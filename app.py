from flask import Flask, request, send_file
import subprocess
import tempfile
import os
from pathlib import Path

app = Flask(__name__)

@app.route("/generate-pdf", methods=["POST"])
def generate_pdf():
    data_xml = request.files["data"]
    template_filename = request.form.get("template")

    template_xml_path = str(Path("/opt/fop/templates") / template_filename)
    
    data_xml_path, output_pdf_path = [
        tempfile.NamedTemporaryFile(delete=False, suffix=suffix).name
        for suffix in [".xml", ".pdf"]
    ]

    data_xml.save(data_xml_path)
    
    subprocess.run(
        [
            "/opt/fop/fop/fop",
            "-xml",
            data_xml_path,
            "-xsl",
            template_xml_path,
            "-pdf",
            output_pdf_path,
        ],
        check=True,
    )

    response = send_file(
        output_pdf_path, download_name="output.pdf", as_attachment=True
    )

    Path(data_xml_path).unlink()
    Path(output_pdf_path).unlink()

    return response


if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
