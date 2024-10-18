# FOP Service

## Overview

The FOP Service is a simple application that generates PDF files from XML data and template files using Apache FOP. This service runs in a Docker container and can be accessed via a REST API endpoint.

## How to Pull the Code from GitHub

To get started with the FOP Service, you can clone the repository from GitHub using the following command:

```sh
git clone https://github.com/yourusername/docker-services-fop.git
```

Replace `yourusername` with your GitHub username. After cloning, navigate into the directory:

```sh
cd docker-services-fop
```

## How to Build and Run the App

1. **Build the App**

    To build the Docker images and start the service, run the following commands:

    ```sh
    docker-compose build
    docker-compose up
    ```

    This will build the necessary images and start the service defined in the `docker-compose.yml` file.

2. **Use the Service**

    The service exposes a POST endpoint to generate PDFs from XML files. You can use the following template for making a request:

    - **Template**

    ```sh
    curl -X POST -F "data=@[path to data file]" -F "template=[template name]" http://localhost:[port defined in env file 52000 is default]/generate-pdf --output [path to output]
    ```

    - **Example**

    Here’s an example of how to use the service with sample XML files:

    ```sh
    curl -X POST -F "data=@/Users/main/Projects/Docker/fop/test-data/2024070001 - AND (Applied Novel Devices).xml" -F "template=invoice.xml" http://localhost:52000/generate-pdf --output result.pdf
    ```

## Sample Client Function

You can also interact with the FOP Service programmatically using the `generate_pdf` function provided in the `pdf_generator.py` file. This function takes the paths to the data XML, template XML, and the output PDF file as arguments.

### Example Usage of the Client Function

```python
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
    with open(data_xml_path, 'rb') as data_file, open(template_xml_path, 'rb') as template_file:
        response = requests.post(url, files={'data': data_file, 'template': template_file})
    
    with open(output_pdf_path, 'wb') as output_file:
        output_file.write(response.content)

# Example usage
generate_pdf(
    "/Users/main/Desktop/data.xml",
    "/Users/main/Desktop/template.xml",
    "/Users/main/Desktop/result.pdf"
)
```

## Using the Docker Image from Docker Hub

If you want to use the pre-built Docker image from Docker Hub, you can pull it directly with the following command:

```sh
docker pull overtime0022/fop-service:latest
```

### Running the Docker Image

Once you have pulled the image, you can run it using Docker. Here’s a basic command to run the image, mapping the necessary ports:

```sh
docker run -d -p 52000:50000 overtime0022/fop-service:latest
```

This will start the FOP Service, making it accessible at `http://localhost:52000/generate-pdf`.

## Docker and Docker Compose

- **Dockerfile**: The Dockerfile defines the environment for the FOP Service, including the base image, dependencies, and the command to run the application. It installs Apache FOP and Flask, sets up the working directory, and specifies how to run the Flask application.

- **docker-compose.yml**: The Docker Compose file simplifies the management of multi-container applications. In this case, it defines the PDF generator service, specifies how to build the container, and maps the ports. It also allows for easy configuration of environment variables, such as the port the service will run on.

## Dependencies

To install dependencies for the FOP Service, you can use the provided `requirements.txt` file. This file contains all the necessary Python packages needed for the application. Install the dependencies using the following command:

```sh
pip install -r requirements.txt
```

## Git Ignore

The repository includes a `.gitignore` file that ignores the `venv` directory, ensuring that virtual environment files are not tracked in version control.

By using Docker and Docker Compose, you can easily set up, run, and manage the FOP Service in a consistent environment.
