import httpResponse

class Endpoint:
    # Python's default arguments are evaluated once when the function is defined
    def __init__(self, func=None):
        self.func = func

    def response(self):
        if self.func:
            return str(httpResponse.HttpResponse(200, self.func()))
        else:
            return str(httpResponse.HttpResponse(400))