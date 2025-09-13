from pathlib import Path

from file import DirectoryNotFound, InputFolderSetup, OutputFolderSetup
from logger import logger
from processes import ImageProcessor


def main():
    try:
        input_folder = InputFolderSetup(
            dir=Path("./input"), allowed_extensions={".jpg", ".png"}
        )
    except (
        DirectoryNotFound,
        ValueError,
    ) as error:
        logger.error(error)
        raise

    try:
        output_folder = OutputFolderSetup(dir=Path("./output"))
    except (DirectoryNotFound) as error:
        logger.error(error)
        raise

    output_folder.cleanup()
    processor = ImageProcessor(input_folder=input_folder, output_folder=output_folder)

    for file in input_folder.files:
        processor.optimize_image(file)
    else:
        logger.info("All images are processed!")


if __name__ == "__main__":
    main()
