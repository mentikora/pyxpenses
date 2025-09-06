from PIL import Image
from dataclasses import dataclass
from pathlib import Path
from logger import logger

@dataclass
class ImageProcessor():
    input_folder: Path
    output_folder: Path
    
    def rescale(self, image: Image, format: tuple[int, int]) -> None:
        pass
    
    def optimize_image(self, file: Path, quality: int = 80, method: int = 6 ) -> None:
        
        with Image.open(file) as img:
            current = img.convert('RGB')
            
            output_path = self.output_folder.dir / (file.stem + ".webp")

            current.save(
                output_path,
                "WEBP",
                optimize=True,
                quality=quality,
                method=method
            )

            logger.info(f"Processed: {file.name} -> {output_path.name}")
            
