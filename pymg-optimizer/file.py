from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from logger import logger


class DirectoryNotFound(Exception):
    """Raised when directory is missing"""

    pass


@dataclass
class ABCFolderSetup(ABC):
    dir: Optional[Path] = None

    def __post_init__(self):
        if isinstance(self.dir, str):
            self.dir = Path(self.dir)

    @abstractmethod
    def _check_directory() -> None:
        raise NotImplementedError


@dataclass
class OutputFolderSetup(ABCFolderSetup):
    def __post_init__(self):
        super().__post_init__()
        self._check_directory()
        logger.info("Output folder is setupped")

    def _check_directory(self) -> None:
        if not self.dir.exists():
            self.dir.mkdir(parents=True, exist_ok=True)

    def cleanup(self) -> None:
        for file in self.dir.iterdir():
            if file.is_file():
                file.unlink()
        logger.info("Cleanup output folder...")


@dataclass
class InputFolderSetup(ABCFolderSetup):
    allowed_extensions: Optional[set[str]] = None

    def __post_init__(self):
        super().__post_init__()

        self._check_directory()
        self._get_files()

        logger.info("Input folder is setupped")

    def _check_directory(self) -> None:
        if not self.dir.is_dir():
            raise DirectoryNotFound(f"Required directory is missing: {self.dir}")

    def _get_files(self) -> None:
        files = []

        for file in self.dir.iterdir():
            if file.is_file() and file.suffix.lower() in self.allowed_extensions:
                files.append(file)
            else:
                logger.info(f"{file} would not be processed")

        self._files = files

    @property
    def files(self) -> list[any]:
        return self._files
