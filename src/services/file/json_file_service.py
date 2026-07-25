"""
Project : Invoice Generator
Project ID : 013

JSON File Service
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class JsonFileService:
    """
    Performs JSON file operations.

    This service is responsible only for reading and
    writing JSON files. It contains no business logic
    and has no knowledge of invoice models.
    """

    @staticmethod
    def save_json(
        file_path: str | Path,
        data: dict[str, Any],
    ) -> None:
        """
        Saves a dictionary as a JSON file.
        """

        path = Path(file_path)

        if path.parent:
            path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

        with path.open(
            mode="w",
            encoding="utf-8",
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
            )

    @staticmethod
    def load_json(
        file_path: str | Path,
    ) -> dict[str, Any]:
        """
        Loads a JSON file.

        Returns
        -------
        dict[str, Any]
        """

        path = Path(file_path)

        with path.open(
            mode="r",
            encoding="utf-8",
        ) as file:

            return json.load(file)

    @staticmethod
    def file_exists(
        file_path: str | Path,
    ) -> bool:
        """
        Returns True if the file exists.
        """

        return Path(file_path).is_file()

    @staticmethod
    def create_directory(
        directory: str | Path,
    ) -> None:
        """
        Creates a directory if it does not exist.
        """

        Path(directory).mkdir(
            parents=True,
            exist_ok=True,
        )

    @staticmethod
    def get_json_extension() -> str:
        """
        Returns the standard JSON extension.
        """

        return ".json"


# ------------------------------------------------------------------
# Public Methods
# ------------------------------------------------------------------

# JsonFileService.save_json(file_path, data)
# JsonFileService.load_json(file_path)
# JsonFileService.file_exists(file_path)
# JsonFileService.create_directory(directory)
# JsonFileService.get_json_extension()

# ------------------------------------------------------------------
# Public Signals
# ------------------------------------------------------------------

# None

# ------------------------------------------------------------------
# Dependencies
# ------------------------------------------------------------------

# json
# pathlib
# typing