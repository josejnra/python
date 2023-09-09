from typing import List, Callable
from logging import Filter, LogRecord
import logging


class RedactingFilter(Filter):
    def __init__(self, patterns: List[str]):
        super().__init__()
        self._patterns = patterns

    def filter(self, record) -> bool:
        record.msg = self.redact(record.msg)
        if isinstance(record.args, dict):
            for k in record.args.keys():
                record.args[k] = self.redact(record.args[k])
        else:
            record.args = tuple(self.redact(arg) for arg in record.args)
        return True

    def redact(self, msg: str) -> str:
        for pattern in self._patterns:
            msg = msg.replace(pattern, "<<TOP SECRET!>>")
        return msg


def filter_maker(level: str) -> Callable[[str], bool]:
    """filter factory function"""
    level = getattr(logging, level)

    def msg_filter(record: LogRecord) -> bool:
        return record.levelno <= level

    return msg_filter
