"""
@author Yonas Gebregziabher

This class provides functionality to get image rgb data, 
manipulate pixels, as well as generate a final image
object.
"""

from PIL import Image, ImageDraw, ImageFont
from typing import List

LEFT_OFFSET = 55
RIGHT_OFFSET = 55
TOP_OFFSET = 68
BOTTOM_OFFSET = 217


class ImageProcessor:

    def __init__(self, image_path: str) -> None:
        "Constructor to create an ImageProcessor object"
        self.image, self.rgb_data = self.get_image(image_path)

    def get_image(self, image_path: str) -> tuple:
        "Returns rgb pixel data and the image object"
        image = Image.open(image_path)
        return image, list(image.getdata())

    def calculate_brightness_factor(self, tempo: int) -> float:
        "Calculates a factor to multiply pixels by"
        min_brightness, max_brightness = 0.5, 1.8  # custom range
        min_tempo, max_tempo = 80, 150

        tempo = max(min(tempo, max_tempo), min_tempo)
        brightness_factor = ((tempo - min_tempo) / (max_tempo - min_tempo)) * \
            (max_brightness - min_brightness) + min_brightness

        return brightness_factor

    def adjust_pixel_rgb(self, rgb_data: List[tuple], tempo: int) -> List[tuple]:
        "Manipulates pixels based on tempo of the song"
        adjusted_image_data = []
        brightness_factor = self.calculate_brightness_factor(tempo)
        for pixel in rgb_data:
            r, g, b = pixel
            r = int(r * brightness_factor)
            g = int(g * brightness_factor)
            b = int(b * brightness_factor)
            # ensures multiplying it doesn't cause invalid rgb value
            r = min(max(r, 0), 255)
            g = min(max(g, 0), 255)
            b = min(max(b, 0), 255)
            adjusted_image_data.append((r, g, b))

        return adjusted_image_data

    def gen_img_from_rgb(self, rgb_data: List[tuple], song_title: str, tempo: int, image_size: List):
        "Layers on manipulated image on polaroid frame and adds song title"
        adjusted_image_data = self.adjust_pixel_rgb(
            rgb_data, tempo)
        adjusted_image = Image.new("RGB", (image_size[0], image_size[1]))
        adjusted_image.putdata(adjusted_image_data)

        base_img = Image.open("assets/layer_photo.png")
        right, bottom = base_img.width - RIGHT_OFFSET, base_img.height - BOTTOM_OFFSET

        overlay_img = adjusted_image.resize(
            (right-LEFT_OFFSET, bottom-TOP_OFFSET))
        # fit into layer_photo picture frame position
        base_img.paste(overlay_img, (LEFT_OFFSET, TOP_OFFSET))

        draw = ImageDraw.Draw(base_img)
        font = ImageFont.truetype("assets/handwrite_font.ttf", 80)
        bbox = font.getbbox(song_title)
        position = (base_img.width - bbox[2] -
                    20, base_img.height - bbox[3] - 75)
        draw.text(position, song_title, font=font, fill=(0, 0, 0))
        output_file_name = song_title.replace(" ", "_")
        base_img.save(f"examples/{output_file_name}.png")
        return base_img
