from pathlib import Path
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from utilities.writer import write_txt


class HtmlTemplate:
    def __init__(self, file, name):
        # Create a html template object and substitute variables in the template
        html_file = (Template(Path(file).read_text())).substitute({"name": name})

        # Create html message
        self.html_message = MIMEMultipart()
        self.html_message.attach(MIMEText(html_file, "html"))

    def add_image(self, image, content_id):
        try:
            with open(image, "rb") as file:
                image_data = file.read()
                image = MIMEImage(image_data)
                image.add_header("Content-ID", content_id)  # <image>
                # image.add_header("Contend-ID", "<paypal>")
                self.html_message.attach(image)
        except:
            write_txt("Unable to open assets directory")
            raise FileNotFoundError(f"Unable to open assets directory")
