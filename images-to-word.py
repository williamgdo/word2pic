from PIL import Image, ImageDraw, ImageFont
from unidecode import unidecode

def process_text(text):
    # Remove accents
    text = unidecode(text)
    # Replace spaces with hyphens
    text = text.replace(" ", "-")
    # Convert text to lowercase
    text = text.lower()
    return text

# List of words to save as images
words = ["Apple", "Banana", "Pineapple Pizza"]

# sorted_words = words.sort()

# Set up font and image size
font_small = ImageFont.truetype("C:/Windows/Fonts/NotoMono-Regular.ttf", 36)
font_big = ImageFont.truetype("C:/Windows/Fonts/NotoMono-Regular.ttf", 60)
image_size = (500, 300)

# Create and save an image for each word
for word in words:
    # Create a new image with a white background
    image = Image.new("RGB", image_size, "black")
    draw = ImageDraw.Draw(image)
    
    # Calculate the position for the text
    x = (image.width) / 2 - (len(word) * 11)
    y = (image.height) / 2 - 22
    text_position_small = (x, y)

    x = (image.width) / 2 - (len(word) * 18)
    y = (image.height) / 2 - 30
    text_position_big = (x, y)
    
    if len(word) < 13:
        draw.text(text_position_big, text=word.upper(), font=font_big, fill=(255, 255, 255))
    else:
        draw.text(text_position_small, text=word.upper(), font=font_small, fill=(255, 255, 255))
        
    # Add the text to the image
    # draw.text(text_position, word, font=font, fill="black")
    
    # Save the image
    image.save(f"images/{process_text(word)}.png")