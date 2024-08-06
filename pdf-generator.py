import requests

def generate_pdf(data_xml_path, template_xml_path, output_pdf_path, url="http://localhost:52000/generate-pdf"):
    """
    Generate a PDF file by sending XML data and template to a specified URL.

    Parameters:
        data_xml_path (str): The file path to the XML data file.
        template_xml_path (str): The file path to the XML template file.
        output_pdf_path (str): The file path where the generated PDF will be saved.
        url (str): The URL endpoint for generating the PDF. Defaults to "http://localhost:52000/generate-pdf".
    """
    # Prepare files for the POST request
    with open(data_xml_path, 'rb') as data_file, open(template_xml_path, 'rb') as template_file:
        response = requests.post(url, files={'data': data_file, 'template': template_file})

    # Save the generated PDF
    with open(output_pdf_path, 'wb') as output_file:
        output_file.write(response.content)

# Example usage
generate_pdf(
    "/Users/main/Desktop/data.xml",
    "/Users/main/Desktop/template.xml",
    "/Users/main/Desktop/prettyendresult.pdf"
)