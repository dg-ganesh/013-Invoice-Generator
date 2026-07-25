"""
Project : Invoice Generator
Project ID : 013

Application Entry Point
"""

from src.services.logging.execution_logging_service import (
    get_execution_logger,
)
from src.ui.main_window import MainWindow


def main() -> None:
    """
    Application bootstrap.

    Initializes runtime logging, launches the main
    application window, and generates the execution report.
    """

    logger = get_execution_logger()

    try:
        logger.start_execution()

        logger.checkpoint("Execution logging initialized")

        application = MainWindow()

        logger.checkpoint("Main window created")

        logger.checkpoint("Application entering event loop")

        application.run()

        logger.checkpoint("Application closed normally")

    except Exception as error:
        logger.fail_execution(error)
        raise

    finally:
        logger.finish_execution()


if __name__ == "__main__":
    main()