"""
Project : Invoice Generator
Project ID : 013

Execution Logging Service
"""

from __future__ import annotations

import time
from datetime import datetime

from src import config


class ExecutionLoggingService:
    """
    Generates the runtime execution report used to verify
    application execution during development.
    """

    def __init__(self) -> None:
        self._start_time: float | None = None
        self._start_datetime: datetime | None = None
        self._checkpoints: list[str] = []
        self._status = "PASS"
        self._error_message = ""

    # --------------------------------------------------------------
    # Public Methods
    # --------------------------------------------------------------

    def start_execution(self) -> None:
        """
        Starts execution tracking.
        """
        config.LOGS_FOLDER.mkdir(parents=True, exist_ok=True)

        self._start_time = time.perf_counter()
        self._start_datetime = datetime.now()

        self.checkpoint("Application execution started")

    def checkpoint(self, message: str) -> None:
        """
        Records a successful execution checkpoint.
        """
        timestamp = datetime.now().strftime(config.DATETIME_FORMAT)
        self._checkpoints.append(f"[{timestamp}] {message}")

    def fail_execution(self, error: Exception | str) -> None:
        """
        Marks the execution as failed.
        """
        self._status = "FAIL"
        self._error_message = str(error)

    def finish_execution(self) -> None:
        """
        Completes execution tracking and writes
        the execution report.
        """
        duration = 0.0

        if self._start_time is not None:
            duration = time.perf_counter() - self._start_time

        report_lines = [
            "=" * 60,
            f"Project              : {config.PROJECT_NAME}",
            f"Project ID           : {config.PROJECT_ID}",
            f"Application Version  : {config.APPLICATION_VERSION}",
            "=" * 60,
            "",
            f"Execution Start      : {self._format_datetime()}",
            f"Execution Status     : {self._status}",
            "",
            "Execution Checkpoints",
            "-" * 60,
        ]

        if self._checkpoints:
            report_lines.extend(self._checkpoints)
            last_checkpoint = self._checkpoints[-1]
        else:
            report_lines.append("No checkpoints recorded.")
            last_checkpoint = "None"

        report_lines.extend(
            [
                "",
                "-" * 60,
                f"Last Successful Checkpoint : {last_checkpoint}",
            ]
        )

        if self._status == "FAIL":
            report_lines.extend(
                [
                    "",
                    "Error Information",
                    "-" * 60,
                    self._error_message,
                ]
            )

        report_lines.extend(
            [
                "",
                f"Execution Duration : {duration:.3f} seconds",
                "=" * 60,
            ]
        )

        config.EXECUTION_REPORT_FILE.write_text(
            "\n".join(report_lines),
            encoding=config.DEFAULT_ENCODING,
        )

    # --------------------------------------------------------------
    # Private Methods
    # --------------------------------------------------------------

    def _format_datetime(self) -> str:
        """
        Formats the execution start time.
        """
        if self._start_datetime is None:
            return "N/A"

        return self._start_datetime.strftime(config.DATETIME_FORMAT)


# ------------------------------------------------------------------
# Public Factory
# ------------------------------------------------------------------

_execution_logger = ExecutionLoggingService()


def get_execution_logger() -> ExecutionLoggingService:
    """
    Returns the shared execution logging service.
    """
    return _execution_logger


# ------------------------------------------------------------------
# Public Methods
# ------------------------------------------------------------------

# ExecutionLoggingService.start_execution()
# ExecutionLoggingService.checkpoint(message)
# ExecutionLoggingService.fail_execution(error)
# ExecutionLoggingService.finish_execution()
# get_execution_logger()

# ------------------------------------------------------------------
# Public Signals
# ------------------------------------------------------------------

# None

# ------------------------------------------------------------------
# Dependencies
# ------------------------------------------------------------------

# src.config
# datetime
# pathlib (via config)
# time