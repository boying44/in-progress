statusCode = {
    200:'OK',
    
}

class HttpResponse:
    def __init__(self, status, body=''):
        self.status = status
        self.body = body

    def __str__(self):
        return f'HTTP/1.1 {self.status} OK\n\n{self.body}\n'