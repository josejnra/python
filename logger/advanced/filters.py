from logging import Filter
from typing import List


class RedactingFilter(Filter):

    def __init__(self, patterns: List[str]):
        super().__init__()
        self._patterns = patterns

    def filter(self, record):
        record.msg = self.redact(record.msg)
        if isinstance(record.args, dict):
            for k in record.args.keys():
                record.args[k] = self.redact(record.args[k])
        else:
            record.args = tuple(self.redact(arg) for arg in record.args)
        return True

    def redact(self, msg: str):
        for pattern in self._patterns:
            msg = msg.replace(pattern, "<<TOP SECRET!>>")
        return msg
