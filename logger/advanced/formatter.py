import logging
import re

class SensitiveFormatter(logging.Formatter):
    """Formatter that removes sensitive information in urls."""

    def format(self, record):
        original = logging.Formatter.format(self, record)
        return self._filter(original)

    @staticmethod
    def _filter(string):
        return re.sub(
            r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+",
            "[EMAIL REDACTED]",
            string
        )
