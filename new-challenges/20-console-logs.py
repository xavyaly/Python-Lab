#!/usr/bin/python23

import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Logging some messages
logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")

# Fetch logs from the console
logger = logging.getLogger()
for handler in logger.handlers:
    if hasattr(handler, 'stream'):
        handler.stream.flush()

