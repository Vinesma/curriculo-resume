from jinja2 import FileSystemLoader, Environment
from time import localtime
import json, subprocess

with open("./data/ptbr.json") as dataFile:
    data = json.load(dataFile)

year, month, day = localtime()[:3]
name = data['nome']
filename_pdf_pt = f"Curriculo - {name} {day}-{month}-{year}.pdf"
filename_pdf_en = f"Resume - {name} {day}-{month}-{year}.pdf"

def renderFromTemplate(directory, template_name, **kwargs):
    loader = FileSystemLoader(directory)
    env = Environment(loader=loader)
    template = env.get_template(template_name)
    return template.render(**kwargs)

with open("resume.html", "w") as resume:
    resume.write(renderFromTemplate("./template", "template1.html", **data))

# Convert to pdf
subprocess.run(["wkhtmltopdf", "--enable-local-file-access", "-B", "0", "-L", "0", "-R", "0", "-T", "0", "resume.html", filename_pdf_pt], check=True)
