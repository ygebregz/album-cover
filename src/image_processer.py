"""
This class extracts image data
"""

from PIL import Image
from typing import List


class ImageProcesser:

    def __init__(self) -> None:
        pass

    def get_rgb_data(self, image_path: str):
        image = Image.open(image_path)
        return list(image.getdata())

    def gen_img_from_rgb(self, rgb_data: List[tuple], song_title: str):
        pass

    def adjust_pixel_rgb(self, rgb_data: List[tuple], tempo: int):
        pass

    def save_image(self, image, file_name: str):
        file_name = f"images/outputs/{file_name}"
        image.save(fp=file_name)
