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
        pix = page.get_pixmap(alpha=False, dpi=300)
        
        # Convert image to PIL Image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        # Save the image as PNG
        path = f"{output_path}_page_{page_number + 1}.png"
        img.save(path, "PNG")
        
        slide_object = {
            "path": path,
            "squashed": False
        }
        json["slides"].append(slide_object)

    # Close the PDF
    pdf_document.close()

    return json

# # Example usage
# pdf_path = 'RL 1.4 MDPs (1).pdf'
# output_path = './split_db/output_image'
# convert_pdf_to_png(pdf_path, output_path)