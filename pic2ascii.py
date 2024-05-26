import requests
from PIL import Image
from io import BytesIO

# ASCII characters used to build the output text
ASCII_CHARS = "@%#*+=-:. "

def fetch_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    return image

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    return image.convert("L")

def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 32] for pixel in pixels])
    return ascii_str

def image_to_ascii(url, width=100):
    image = fetch_image(url)
    image = resize_image(image, width)
    image = grayscale_image(image)
    
    ascii_str = pixel_to_ascii(image)
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join([ascii_str[index: index + img_width] for index in range(0, ascii_str_len, img_width)])
    
    return ascii_img

def main():
    url = input("Enter the URL of the image: ")
    width = int(input("Enter the width of the ASCII art (default 100): ") or 100)
    ascii_art = image_to_ascii(url, width)
    print(ascii_art)

if __name__ == "__main__":
    main()
