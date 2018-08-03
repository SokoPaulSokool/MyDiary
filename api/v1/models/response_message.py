import json
from flask import Response


class ResponseMessage():
    """Simplifies api response

    Keyword arguments: message, code
    message -- data to be returned to the user
    code -- status code of the response 
    """
    def __init__(self, message, code):
        self.message = message
        self.code = code

    def response(self):
        res = {"message": self.message}, self.code
        return res
