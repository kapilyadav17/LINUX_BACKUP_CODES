from PIL import Image
import os

def make_square(image_path, output_path, size=500):
    img = Image.open(image_path)
    width, height = img.size

    if width == height:
        img = img.resize((size, size))
    else:
        new_size = max(width, height)
        new_img = Image.new("RGB", (new_size, new_size), (255, 255, 255))
        new_img.paste(img, ((new_size - width) // 2, (new_size - height) // 2))
        img = new_img.resize((size, size))

    img.save(output_path)
    return output_path
