import os
import sys
import logging.handlers

LOGLEVEL = os.getenv("LOGLEVEL", "INFO").upper()

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(LOGLEVEL)

# File Handler
LOG_FILE = "script.log"
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1048576, backupCount=5)
handler.setLevel(logging.INFO)

# Stream Handler
stream_handler = logging.StreamHandler(stream=sys.stdout)
stream_handler.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter("%(asctime)s %(process)s %(thread)s - %(name)s - %(levelname)s - %(message)s")

# Add Formatter to Handlers
handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# add Handlers to Logger
logger.addHandler(handler)
logger.addHandler(stream_handler)
