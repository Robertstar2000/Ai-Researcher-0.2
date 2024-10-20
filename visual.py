# visual.py

# This module handles visual generation.

import os
from PIL import Image, ImageDraw, ImageFont
from settings import groq_api_call
from style import get_visual_style_prompt

def generate_visual(description, title):
    """
    Generates a visual image based on the description.

    Args:
        description (str): The description of the visual content.
        title (str): The title of the section (used for naming the image file).

    Returns:
        str: The path to the generated image file.
    """
    # Get the style prompt for visuals.
    visual_style_prompt = get_visual_style_prompt()

    # Form the prompt for the AI model.
    prompt = f"{visual_style_prompt}\n\nCreate a visual representation of the following description:\n\n{description}"

    # Call the AI API to get the visual input.
    visual_input = groq_api_call(prompt)

    # Use Pillow to generate an image based on the visual_input.
    # For simplicity, we'll create a simple image with text.
    img = Image.new('RGB', (800, 600), color=(255, 255, 255))
    d = ImageDraw.Draw(img)

    # Load a font.
    font = ImageFont.load_default()

    # Wrap text to fit the image width.
    text = visual_input
    lines = []
    words = text.split(' ')
    line = ''
    for word in words:
        if d.textsize(line + ' ' + word, font=font)[0] < 780:
            line += ' ' + word
        else:
            lines.append(line)
            line = word
    lines.append(line)

    y_text = 50
    for line in lines:
        d.text((10, y_text), line, fill=(0, 0, 0), font=font)
        y_text += 15

    # Ensure the visuals directory exists.
    visuals_dir = 'visuals'
    if not os.path.exists(visuals_dir):
        os.makedirs(visuals_dir)

    # Save the image with a filename based on the section title.
    image_path = os.path.join(visuals_dir, f"{title.replace(' ', '_')}.png")
    img.save(image_path)

    return image_path