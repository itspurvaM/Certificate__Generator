
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

# --- Configuration ---
TEMPLATE_PATH = 'GFG_template.png'
NAMES_FILE = 'names.csv'
FONT_PATH = 'your_font.ttf' # Replace with your font file name
OUTPUT_DIR = 'generated_certificates'

# Text properties (adjust these based on your template's design)
FONT_SIZE = 50
TEXT_COLOR = (0, 0, 0) # Black color (RGB)

# Coordinates for the name (X, Y) - You'll need to find these by trial and error
# X is the horizontal position, Y is the vertical position.
# (0, 0) is the top-left corner of the image.
NAME_CENTER_X = 775 # Example value for centering horizontally
NAME_CENTER_Y = 613 # Example value for vertical placement

# --- Functions ---

def generate_certificate(name, template_img, font):
    """Generates a single certificate for a given name."""
    
    # Create a fresh copy of the template for each certificate
    img = template_img.copy() 
    draw = ImageDraw.Draw(img)
    
    # Calculate text width for centering
    # Use textbbox to get bounding box for accurate centering
    bbox = draw.textbbox((0, 0), name, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Calculate starting X-coordinate for centered text
    # Assuming NAME_CENTER_X is the desired center point
    x_position = NAME_CENTER_X - (text_width / 2)
    y_position = NAME_CENTER_Y - (text_height / 2) # Adjust based on template
    
    # Draw the text on the image
    draw.text((x_position, y_position), name, fill=TEXT_COLOR, font=font)
    
    # Define output file path
    output_filename = os.path.join(OUTPUT_DIR, f"{name.replace(' ', '_')}_Certificate.pdf")
    
    # Save the certificate as a PDF
    # Note: Pillow can save images as PDFs directly.
    img.save(output_filename, "PDF", resolution=100.0)
    print(f"Generated: {output_filename}")


# --- Main Execution ---

if __name__ == "__main__":
    
    # 1. Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    try:
        # 2. Load the list of names
        df = pd.read_csv(NAMES_FILE)
        names = df['Name'].tolist()
        
        # 3. Load the template image and font
        template = Image.open(TEMPLATE_PATH).convert("RGB") # Convert to RGB for better PDF saving
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
        
        print(f"Found {len(names)} names. Starting generation...")
        
        # 4. Loop through names and generate certificates
        for name in names:
            generate_certificate(name, template, font)
            
        print("\nCertificate generation complete!")

    except FileNotFoundError as e:
        print(f"Error: One or more required files not found: {e}")
        print("Please check TEMPLATE_PATH, NAMES_FILE, and FONT_PATH.")
    except KeyError:
        print(f"Error: The '{NAMES_FILE}' file must have a column named 'Name'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")