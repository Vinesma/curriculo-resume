# Currículo / Resume

![render-page](https://github.com/Vinesma/curriculo-resume/workflows/render-page/badge.svg)

[PT/BR] Esse repositório contém templates para gerar meu currículo em Português e Inglês.

[EN] This repository contains templates to generate my resume in both Portuguese and English.

## Como funciona / How it works

[PT/BR] Utilizo a *template engine* [jinja2](https://jinja.palletsprojects.com/en/master/) para ler e popular um template com os dados providos de um arquivo `.json`. Um script python faz tudo isso e ainda gera um `.pdf` com meu nome e a data atual usando [wkhtmltopdf](https://wkhtmltopdf.org/index.html), se estiver instalado.

Quando eu faço um *commit*, uma *Action* do GitHub se responsabiliza por renderizar meu currículo e [hostear no GitHub pages.](https://vinesma.github.io/curriculo-resume/)

[EN] I use the [jinja2](https://jinja.palletsprojects.com/en/master/) template engine to read and populate a template with data provided from a `.json` file. A python script handles all of this and also generates a `.pdf` file with my name and current date using [wkhtmltopdf](https://wkhtmltopdf.org/index.html), if installed.

When I make a commit, a GitHub Action is responsible for rendering my resume and [hosting it on GitHub pages.](https://vinesma.github.io/curriculo-resume/)

## Licenças / Licenses

The icons used are courtesy of [Font Awesome.](https://fontawesome.com/license/free) Nothing was changed from the original files.
