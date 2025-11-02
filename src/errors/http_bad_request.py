
# classe de erro para HTTP 400 Bad Request
class HttpBadRequestError(Exception):
    """Exception raised for HTTP 400 Bad Request errors."""

    # Inicializa a exceção com uma mensagem de erro    
    def __init__(self, message: str) -> None:
        self.message = message
        self.name = 'BadRequest'
        self.status_code = 400