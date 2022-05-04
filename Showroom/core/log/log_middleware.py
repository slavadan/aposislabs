import logging


class LogMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logging.basicConfig(filename="requests.log", level=logging.INFO)
        logging.info(request)
        response = self.get_response(request)
        return response
