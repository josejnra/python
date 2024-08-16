import json
import sys
from loguru import logger


def serialize(record):
    subset = {
        "timestamp": record["time"].timestamp(),
        "message": record["message"],
        "level": record["level"].name,
        "file": record["file"].name,
        "context": record["extra"],
    }
    return json.dumps(subset)


def patching(record):
    record["extra"]["serialized"] = serialize(record)


logger.remove(0)  # remove the default handler configuration

logger = logger.patch(patching)
logger.add(sys.stderr, format="{extra[serialized]}")
# logger.add("logs.log", encoding="utf8")
# logger.add(sys.stdout, level="INFO", serialize=True)
# logger.add(sys.stdout, level="TRACE", colorize=True)
# logger.add(sys.stdout, level="TRACE", format="{time} {level} {message}", colorize=True)
# logger.add(sys.stdout, level="TRACE", format="[{time}] [{process}] [{thread}] [{name}] [{level}] - {message}", colorize=True)

# rotation
# logger.add("file_{time}.log")
# logger.add("file_1.log", rotation="500 MB")  # Automatically rotate too big file
# logger.add("file_2.log", rotation="12:00")  # New file is created each day at noon
# logger.add("file_3.log", rotation="1 week")  # Once the file is too old, it's rotated
# logger.add("file_X.log", retention="10 days")  # Cleanup after some time
# logger.add("file_Y.log", compression="zip")  # Save some loved space


# logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")
