from jinja2 import FileSystemLoader, Environment
from time import localtime
import json, subprocess, os

def load_from_json(path):
    with open(path) as open_file:
        return json.load(open_file)

def deduce_age(current_year, year_birth):
    return current_year - year_birth

def create_filename(prefix, name, day, month, year):
    return f"{prefix} - {name} {day}-{month}-{year}.pdf"

def renderFromTemplate(directory, template_name, **kwargs):
    """ Render the html
    """
    loader = FileSystemLoader(directory)
    env = Environment(loader=loader)
    template = env.get_template(template_name)
    return template.render(**kwargs)

def write_to_html(filename, template_name, **kwargs):
    """ Convert a template into a html file using the data provided.
    """
    with open(filename, "w") as open_file:
        open_file.write(renderFromTemplate("./template", template_name, **kwargs))

def convert_to_pdf(filename, output_filename):
    """ Convert html to pdf if wkhtmltopdf is present in the system.
    """
    if os.path.exists(os.path.join("/", "usr", "bin", "wkhtmltopdf")):
        subprocess.run(["wkhtmltopdf", "--enable-local-file-access", "-B", "0", "-L", "0", "-R", "0", "-T", "0", filename, output_filename], check=True)

def main():
    # Get current year, month and day
    year, month, day = localtime()[:3]

    # Load data
    data = load_from_json("./data/ptbr.json")
    locale = load_from_json("./data/locale_ptbr.json")
    locale_en = load_from_json("./data/locale_en.json")
    # Merge personal data and locale data
    data.update(locale)

    # Convert year into current age
    data['idade'] = deduce_age(year, data['idade'])
    # Retrieve some data to create filenames
    name = data['nome']
    filename_pdf_pt = create_filename("Currículo", name, day, month, year)
    filename_pdf_en = create_filename("Resume", name, day, month, year)

    # Templates -> HTML [-> PDF]
    write_to_html("index.html", "template1.html", **data)
    convert_to_pdf("index.html", filename_pdf_pt)

main()
