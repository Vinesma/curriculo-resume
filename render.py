from jinja2 import FileSystemLoader, Environment

data = { "nome": "Otavio Cornelio da Silva",
        "nacionalidade": "Brasileiro",
        "estado_civil": "Solteiro",
        "idade": 23,
        "endereco": "Rua Lagoa das Capivaras, Nº 53, Jardim das Oliveiras",
        "cep": "08111-150",
        "cidade": "São Paulo",
        "estado": "SP"}

def renderFromTemplate(directory, template_name, **kwargs):
    loader = FileSystemLoader(directory)
    env = Environment(loader=loader)
    template = env.get_template(template_name)
    return template.render(**kwargs)

with open("resume.html", "w") as resume:
    resume.write(renderFromTemplate("./template", "template1.html", **data))
