from jinja2 import FileSystemLoader, Environment
from time import localtime
import json, subprocess, os

def load_from_json(path):
    with open(path) as open_file:
        return json.load(open_file)

def deduce_age(year_birth):
    current_year = localtime()[:1][0]
    return current_year - year_birth

def create_filename(prefix, name):
    # Get current year, month and day
    year, month, day = localtime()[:3]
    return f"{prefix} - {name} {day}-{month}-{year}.pdf"

def renderFromTemplate(directory, template_name, **kwargs):
    """ Render the html
    """
    loader = FileSystemLoader(directory)
    env = Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
    template = env.get_template(template_name)
    return template.render(**kwargs)

def write_to_html(filename, template_name, **kwargs):
    """ Convert a template into a html file using the data provided.
    """
    with open(filename, "w") as open_file:
        open_file.write(renderFromTemplate("./template", template_name, **kwargs))
    print(f"TEMPLATE -> HTML: [{filename}]")

def convert_to_pdf(filename, output_filename):
    """ Convert html to pdf if wkhtmltopdf is present in the system.
    """
    if os.path.exists(os.path.join("/", "usr", "bin", "wkhtmltopdf")):
        subprocess.run(["wkhtmltopdf", "--enable-local-file-access", "-B", "0", "-L", "0", "-R", "0", "-T", "0", filename, output_filename], check=True)
    else:
        print("wkhtmltopdf not found, this external program is necessary to render a pdf from the html file.")

def main():
    # Load data
    data = load_from_json("./data/ptbr.json")
    data_en = load_from_json("./data/en.json")
    locale = load_from_json("./data/locale_ptbr.json")
    locale_en = load_from_json("./data/locale_en.json")
    # Merge personal data and locale data
    data.update(locale)
    data_en.update(locale_en)

    # Convert year into current age
    data['idade'] = deduce_age(data['idade'])
    data_en['idade'] = deduce_age(data_en['idade'])
    # Retrieve some data to create filenames
    name = data['nome']
    filename_pdf_pt = create_filename("Currículo", name)
    filename_pdf_en = create_filename("Resume", name)

    # Templates -> HTML [-> PDF]
    ## render portuguese resume
    write_to_html("index.html", "base.html", **data)
    convert_to_pdf("index.html", filename_pdf_pt)
    ## render english resume
    write_to_html("resume.html", "base.html", **data_en)
    convert_to_pdf("resume.html", filename_pdf_en)

main()
