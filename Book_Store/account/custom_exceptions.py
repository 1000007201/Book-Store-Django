
class BaseCustomException(Exception):
    def __init__(self, message, code):
        self.Error = message
        self.Code = code


class FieldError(BaseCustomException):
    pass


class UsernameNotExist(BaseCustomException):
    pass
