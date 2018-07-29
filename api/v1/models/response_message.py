import json
from flask import Response


class ResponseMessage():
    def __init__(self, message, code):
        self.message = message
        self.code = code

    def response(self):
        res = {"message": self.message}, self.code
        return res
