
# classe de erro para HTTP 422 Unprocessable Entity
class HttpUnprocessableEntityError(Exception):
    """Exception raised for HTTP 422 Unprocessable Entity errors."""

    # Inicializa a exceção com uma mensagem de erro    
    def __init__(self, message: str) -> None:
        self.message = message
        self.name = 'UnprocessableEntity'
        self.status_code = 422