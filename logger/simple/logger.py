import os
import logging.handlers

LOGLEVEL = os.getenv("LOGLEVEL", "INFO").upper()

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(LOGLEVEL)

# Handler
LOG_FILE = "script.log"
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1048576, backupCount=5)
handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Add Formatter to Handler
handler.setFormatter(formatter)

# add Handler to Logger
logger.addHandler(handler)
