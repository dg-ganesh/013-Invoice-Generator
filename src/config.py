"""
Project : Invoice Generator
Project ID : 013

Application Configuration
"""

from pathlib import Path

# ------------------------------------------------------------------
# Project Information
# ------------------------------------------------------------------

PROJECT_NAME = "Invoice Generator"
PROJECT_ID = "013"
APPLICATION_VERSION = "1.0.0"

# ------------------------------------------------------------------
# Window Configuration
# ------------------------------------------------------------------

WINDOW_TITLE = f"{PROJECT_NAME} v{APPLICATION_VERSION}"
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 1100
WINDOW_MIN_WIDTH = 1400
WINDOW_MIN_HEIGHT = 950

# ------------------------------------------------------------------
# Folder Configuration
# ------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

ASSETS_FOLDER = PROJECT_ROOT / "assets"
DATA_FOLDER = PROJECT_ROOT / "data"
INPUT_FOLDER = DATA_FOLDER / "input"
OUTPUT_FOLDER = DATA_FOLDER / "output"
SAMPLES_FOLDER = DATA_FOLDER / "samples"

DOCS_FOLDER = PROJECT_ROOT / "docs"
LOGS_FOLDER = PROJECT_ROOT / "logs"
SCREENSHOTS_FOLDER = PROJECT_ROOT / "screenshots"
TESTS_FOLDER = PROJECT_ROOT / "tests"

RELEASES_FOLDER = PROJECT_ROOT / "releases"
BUILD_FOLDER = PROJECT_ROOT / "build"
DIST_FOLDER = PROJECT_ROOT / "dist"

# ------------------------------------------------------------------
# Log Files
# ------------------------------------------------------------------

EXECUTION_REPORT_FILE = LOGS_FOLDER / "execution_report.txt"
APPLICATION_LOG_FILE = LOGS_FOLDER / "application.log"
DEBUG_LOG_FILE = LOGS_FOLDER / "debug.log"

# ------------------------------------------------------------------
# Runtime Configuration
# ------------------------------------------------------------------

DEFAULT_ENCODING = "utf-8"
DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M:%S"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

# ------------------------------------------------------------------
# Public Constants
# ------------------------------------------------------------------

__all__ = [
    "PROJECT_NAME",
    "PROJECT_ID",
    "APPLICATION_VERSION",
    "WINDOW_TITLE",
    "WINDOW_WIDTH",
    "WINDOW_HEIGHT",
    "WINDOW_MIN_WIDTH",
    "WINDOW_MIN_HEIGHT",
    "PROJECT_ROOT",
    "ASSETS_FOLDER",
    "DATA_FOLDER",
    "INPUT_FOLDER",
    "OUTPUT_FOLDER",
    "SAMPLES_FOLDER",
    "DOCS_FOLDER",
    "LOGS_FOLDER",
    "SCREENSHOTS_FOLDER",
    "TESTS_FOLDER",
    "RELEASES_FOLDER",
    "BUILD_FOLDER",
    "DIST_FOLDER",
    "EXECUTION_REPORT_FILE",
    "APPLICATION_LOG_FILE",
    "DEBUG_LOG_FILE",
    "DEFAULT_ENCODING",
    "DATE_FORMAT",
    "TIME_FORMAT",
    "DATETIME_FORMAT",
]