class ServiceException(Exception):
    def __init__(self, code: str, message: str):
        self._code = code
        self._message = message

    @property
    def code(self) -> str:
        return self._code

    @property
    def message(self) -> str:
        return self._message
