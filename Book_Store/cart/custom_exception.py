
class CustomBaseException(Exception):
    def __init__(self, message, code):
        self.Error = message
        self.Code = code


class NullField(CustomBaseException):
    pass


class UserNotExist(CustomBaseException):
    pass


class TokenRequired(CustomBaseException):
    pass


class BookNotExist(CustomBaseException):
    pass

