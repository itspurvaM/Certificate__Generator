# Certificate_Generator
My first project 
certificate generator

🖥️ Overall Purpose
The program automates the creation of personalized certificates. It takes:
- A template image (the certificate background),
- A list of names from a CSV file,
- A font file for styling the text,
 these should be provided in the same directory before running the script
 and then generates a certificate for each person, saving it as a PDF


📌 Summary of What It Does- Reads a list of names from a CSV file.
- Loads a certificate template image and a font.
- For each name:
- Centers the text on the template.
- Draws the name.
- Saves the certificate as a PDF in the output folder.
- Handles common errors gracefully.
