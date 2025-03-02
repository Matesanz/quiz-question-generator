"""Logging module for the application."""
import loguru

logger = loguru.logger


ERROR = logger.error
WARNING = logger.warning
INFO = logger.info
DEBUG = logger.debug
SUCCESS = logger.success
