
class CustomBaseException(Exception):
    def __init__(self, message, code):
        self.Error = message
        self.Code = code


class BookAlreadyExist(CustomBaseException):
    pass


class NullField(CustomBaseException):
    pass


class NotSuperUser(CustomBaseException):
    pass


class TokenRequired(CustomBaseException):
    pass


class UserNotExist(CustomBaseException):
    pass


class BookNotExist(CustomBaseException):
    pass


class CartNotExist(CustomBaseException):
    pass


class FieldError(CustomBaseException):
    pass
