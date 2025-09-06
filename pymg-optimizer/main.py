from pathlib import Path
from PIL import Image
from file import InputFolderSetup, OutputFolderSetup, DirectoryNotFound
from processes import ImageProcessor
from logger import logger

def main():
    try:
        input_folder = InputFolderSetup(
            dir=Path('./input'),
            allowed_extensions={'.jpg', '.png'}
        )
        output_folder = OutputFolderSetup(
            dir=Path('./output')
        )
    except (
        DirectoryNotFound,
        FileNotFoundError,
        ValueError,
    ) as error:
        logger.error(error)

    output_folder.cleanup()
    processor = ImageProcessor(
        input_folder=input_folder,
        output_folder=output_folder
    )
    
    for file in input_folder.files:
        processor.optimize_image(file)
    else:
        logger.info('All images are processed!')


if __name__ == "__main__":
    main()
