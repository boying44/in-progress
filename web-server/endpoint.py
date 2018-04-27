import httpResponse

class Endpoint:
    def __init__(self, path):
        self.path = path

    def response(self):
        return str(httpResponse.HttpResponse(200))