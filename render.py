from jinja2 import FileSystemLoader, Environment
import json

with open("./data/ptbr.json") as dataFile:
    data = json.load(dataFile)

def renderFromTemplate(directory, template_name, **kwargs):
    loader = FileSystemLoader(directory)
    env = Environment(loader=loader)
    template = env.get_template(template_name)
    return template.render(**kwargs)

with open("resume.html", "w") as resume:
    resume.write(renderFromTemplate("./template", "template1.html", **data))
