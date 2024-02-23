import fitz  # PyMuPDF
from PIL import Image

def convert_pdf_to_png(pdf_path, output_path):
    # Open the PDF
    pdf_document = fitz.open(pdf_path)

    json = {
        "num_slides": len(pdf_document),
        "slides": []
    }

    for page_number in range(len(pdf_document)):
        # Get the page
        page = pdf_document.load_page(page_number)
        
        # Render the page as an image
        pix = page.get_pixmap(alpha=False)
        
        # Convert image to PIL Image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        # Save the image as PNG
        path = f"{output_path}_page_{page_number + 1}.png"
        img.save(path, "PNG")
        json["slides"].append(path)

    # Close the PDF
    pdf_document.close()

    return json

# # Example usage
# pdf_path = 'Slides.pdf'
# output_path = './slides_images/output_image'
# convert_pdf_to_png(pdf_path, output_path)