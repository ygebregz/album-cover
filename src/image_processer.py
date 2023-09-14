"""
This class extracts image data
"""

from PIL import Image, ImageDraw, ImageFont
from typing import List


class ImageProcesser:

    def __init__(self) -> None:
        pass

    def get_image(self, image_path: str):
        image = Image.open(image_path)
        return image, list(image.getdata())

    def adjust_pixel_rgb(self, rgb_data: List[tuple], tempo: int):
        adjusted_image_data = []
        brightness_factor = 1.0

        if tempo < 100:
            brightness_factor = 0.8
        elif tempo > 120:
            brightness_factor = 1.9

        for pixel in rgb_data:
            r, g, b = pixel
            r = int(r * brightness_factor)
            g = int(g * brightness_factor)
            b = int(b * brightness_factor)
            r = min(max(r, 0), 255)
            g = min(max(g, 0), 255)
            b = min(max(b, 0), 255)
            adjusted_image_data.append((r, g, b))

        return adjusted_image_data

    def gen_img_from_rgb(self, rgb_data: List[tuple], song_title: str, tempo: int, image_size: List):
        adjusted_image_data = self.adjust_pixel_rgb(
            rgb_data, tempo)
        adjusted_image = Image.new("RGB", (image_size[0], image_size[1]))
        adjusted_image.putdata(adjusted_image_data)

        base_img = Image.open("assets/layer_photo.png")
        left, top = 55, 68
        right, bottom = base_img.width - 55, base_img.height - 217

        overlay_img = adjusted_image.resize((right-left, bottom-top))
        base_img.paste(overlay_img, (left, top))

        draw = ImageDraw.Draw(base_img)
        font = ImageFont.truetype("assets/handwrite_font.ttf", 80)
        bbox = font.getbbox(song_title)
        position = (base_img.width - bbox[2] -
                    15, base_img.height - bbox[3] - 50)
        draw.text(position, song_title, font=font, fill=(0, 0, 0))
        return base_img
