def wsgi_application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    response = environ['QUERY_STRING'].split('&')
    response = [i + '\r\n' for i in response]
    return response