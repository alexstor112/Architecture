from pprint import pprint
from request import Request
from controller import control_func


def application(environ, start_response):
    # print(environ)
    request = Request(environ)
    # print(request.method)
    # print(request.path)
    # print(request.headers)
    # print(request.query_strings)
    # print(request.body)
    start_response('200 OK', [('Content-Type', 'text/html')])
    return control_func(request.method, request.path, request.body)
