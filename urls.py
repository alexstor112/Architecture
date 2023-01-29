
import json

TEMPLATE_PATH = 'templates/'

paths = {
    '/': 'index.html',
    '/about': 'about.html',
}


def url_map(path):
    if path in paths:
        return f'{TEMPLATE_PATH}{paths[path]}'
    return f'{TEMPLATE_PATH}{paths["/"]}'

