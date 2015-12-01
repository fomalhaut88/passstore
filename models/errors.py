class BaseError(Exception):
    pass


class CommandError(BaseError):
    pass


class CommandNotFound(CommandError):
    pass
