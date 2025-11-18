# Calculator API - Advanced Mathematical Operations

A RESTful API built with Flask that provides three distinct mathematical calculators with different computational approaches, featuring comprehensive error handling, clean architecture, and extensive test coverage.

## 🚀 Features

### Three Specialized Calculators

#### Calculator 1 - Complex Number Processing
- Divides a number into three equal parts
- Applies unique mathematical operations to each part:
  - **Part 1**: `((n/4) + 7)² × 0.257`
  - **Part 2**: `(n^2.121) / 5 + 1`
  - **Part 3**: Maintains original value
- Returns the sum of all three results

#### Calculator 2 - Statistical Analysis
- Processes multiple numbers with power operations
- Applies transformation: `(n × 11)^0.95` to each number
- Calculates standard deviation using NumPy
- Returns the inverse of the standard deviation: `1/σ`

#### Calculator 3 - Variance Validation
- Calculates variance of multiple numbers using NumPy
- Computes multiplication of all input numbers
- Validates that variance is greater than multiplication
- Returns success with variance value or error message

### Technical Features
- **Clean Architecture**: Separation of concerns with drivers, errors, and calculators
- **Error Handling**: Custom HTTP exceptions (400, 422) with descriptive messages
- **Dependency Injection**: Interface-based design for NumPy handler
- **Comprehensive Testing**: Unit and integration tests with pytest
- **Type Hints**: Full Python type annotations for better code quality
- **RESTful Design**: JSON-based request/response format

## 🛠️ Tech Stack

- **Framework**: Flask (Python web framework)
- **Scientific Computing**: NumPy for statistical operations
- **Testing**: pytest for automated testing
- **Architecture**: Clean Architecture with dependency injection
- **Type System**: Python type hints throughout

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Basic understanding of REST APIs and statistical concepts

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd calculator-api
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask numpy pytest
   ```

## 🚦 Running the Application

1. **Start the server**
   ```bash
   python run.py
   ```

2. **Access the API**
   - Base URL: `http://localhost:3000`
   - The server will run on port 3000 with debug mode enabled

## 📚 API Documentation

### Calculator 1 - Complex Processing

#### POST /calculator/1
Process a single number through three mathematical operations.

**Request Body:**
```json
{
  "number": 15.5
}
```

**Response (200 OK):**
```json
{
  "data": {
    "Calculator": 1,
    "result": 45.67
  }
}
```

**Mathematical Process:**
1. Input divided by 3: `15.5 / 3 = 5.167`
2. First part: `((5.167/4) + 7)² × 0.257 = 14.25`
3. Second part: `(5.167^2.121) / 5 + 1 = 7.89`
4. Third part: `5.167`
5. Final result: `14.25 + 7.89 + 5.167 = 27.31`

**Error Response (422):**
```json
{
  "errors": [{
    "title": "UnprocessableEntity",
    "detail": "Body mal formatado: 'number' ausente"
  }]
}
```

### Calculator 2 - Statistical Analysis

#### POST /calculator/2
Calculate inverse of standard deviation after transformation.

**Request Body:**
```json
{
  "numbers": [2.12, 4.62, 1.32]
}
```

**Response (200 OK):**
```json
{
  "data": {
    "Calculator": 2,
    "result": 0.08
  }
}
```

**Mathematical Process:**
1. Transform each number: `n × 11)^0.95`
2. Calculate standard deviation: `σ = np.std([transformed_numbers])`
3. Return inverse: `1 / σ`

**Error Response (422):**
```json
{
  "errors": [{
    "title": "UnprocessableEntity",
    "detail": "Body mal formatado: 'numbers' ausente"
  }]
}
```

### Calculator 3 - Variance Validation

#### POST /calculator/3
Validate variance against multiplication of numbers.

**Request Body:**
```json
{
  "numbers": [1, 1, 1, 1, 100]
}
```

**Success Response (200 OK):**
```json
{
  "data": {
    "Calculator": 3,
    "variance": 1568.16,
    "success": true
  }
}
```

**Error Response (400 Bad Request):**
```json
{
  "errors": [{
    "title": "BadRequest",
    "detail": "Resultado inválido: variância menor que multiplicação"
  }]
}
```

**Validation Logic:**
- Calculate variance: `σ² = np.var(numbers)`
- Calculate multiplication: `product = n₁ × n₂ × ... × nₙ`
- Check: `variance > multiplication`
- If false, return 400 error
- If true, return variance with success flag

## 🏗️ Project Architecture

```
calculator-api/
├── run.py                          # Application entry point
├── src/
│   ├── calculators/
│   │   ├── calculator_1.py         # Simple mathematical operations
│   │   ├── calculator_1_test.py    # Unit tests for calculator 1
│   │   ├── calculator_2.py         # Statistical analysis calculator
│   │   ├── calculator_2_test.py    # Integration/unit tests
│   │   ├── calculator_3.py         # Variance validation calculator
│   │   └── calculator_3_test.py    # Unit tests with mocks
│   ├── drivers/
│   │   ├── numpy_handler.py        # NumPy wrapper for operations
│   │   └── interfaces/
│   │       └── driver_handler_interface.py  # Abstract interface
│   ├── errors/
│   │   ├── error_control.py        # Central error handler
│   │   ├── http_bad_request.py     # 400 error class
│   │   └── http_unprocessable_entity.py  # 422 error class
│   └── main/
│       └── server/
│           └── server.py           # Flask server configuration
└── .vscode/
    └── settings.json               # VS Code configuration
```

## 🎯 Architecture Principles

### Clean Architecture
- **Separation of Concerns**: Each calculator is independent
- **Dependency Injection**: NumPy handler injected into calculators
- **Interface Segregation**: Abstract interface for driver handlers
- **Single Responsibility**: Each class has one clear purpose

### Design Patterns
- **Dependency Injection**: Calculators receive driver handler as parameter
- **Factory Pattern**: Error handler creates appropriate error responses
- **Interface Pattern**: DriverHandlerInterface defines contract

### Error Handling
```python
# Custom exception classes
class HttpBadRequestError(Exception):
    status_code = 400
    name = 'BadRequest'

class HttpUnprocessableEntityError(Exception):
    status_code = 422
    name = 'UnprocessableEntity'

# Centralized error handling
def handle_error(error: Exception) -> Dict:
    # Maps exceptions to appropriate HTTP responses
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific calculator tests
pytest src/calculators/calculator_1_test.py
pytest src/calculators/calculator_2_test.py
pytest src/calculators/calculator_3_test.py

# Verbose output
pytest -v
```

### Test Coverage

#### Calculator 1 Tests
- ✅ Valid input processing
- ✅ Invalid body format handling
- ✅ Result accuracy validation

#### Calculator 2 Tests
- ✅ Integration test with real NumPy
- ✅ Unit test with mocked driver
- ✅ Multiple numbers processing

#### Calculator 3 Tests
- ✅ Successful variance validation
- ✅ Failed variance validation (error case)
- ✅ Mock driver implementation

### Example Test Output
```
src/calculators/calculator_1_test.py ✓✓
src/calculators/calculator_2_test.py ✓✓
src/calculators/calculator_3_test.py ✓✓

6 passed in 0.45s
```

## 💡 Usage Examples

### Using curl

```bash
# Calculator 1 - Single number
curl -X POST http://localhost:3000/calculator/1 \
  -H "Content-Type: application/json" \
  -d '{"number": 10}'

# Calculator 2 - Multiple numbers
curl -X POST http://localhost:3000/calculator/2 \
  -H "Content-Type: application/json" \
  -d '{"numbers": [1.5, 2.5, 3.5, 4.5]}'

# Calculator 3 - Variance validation
curl -X POST http://localhost:3000/calculator/3 \
  -H "Content-Type: application/json" \
  -d '{"numbers": [10, 20, 30, 40, 50]}'
```

### Using Python requests

```python
import requests
import json

base_url = "http://localhost:3000"

# Calculator 1
response = requests.post(
    f"{base_url}/calculator/1",
    json={"number": 42}
)
print(response.json())

# Calculator 2
response = requests.post(
    f"{base_url}/calculator/2",
    json={"numbers": [5.5, 10.2, 15.8]}
)
print(response.json())

# Calculator 3
response = requests.post(
    f"{base_url}/calculator/3",
    json={"numbers": [100, 200, 300]}
)
print(response.json())
```

## 🔬 NumPy Integration

### NumpyHandler Class
```python
class NumpyHandler(DriverHandlerInterface):
    def standard_derivation(self, numbers: List[float]) -> float:
        return numpy.std(numbers)
    
    def variance(self, numbers: List[float]) -> float:
        return numpy.var(numbers)
```

### Interface Definition
```python
class DriverHandlerInterface:
    def standard_derivation(self, numbers: List[float]) -> float:
        raise NotImplementedError
    
    def variance(self, numbers: List[float]) -> float:
        raise NotImplementedError
```

## ⚙️ Configuration

### Server Configuration
```python
# run.py
app.run(host='0.0.0.0', port=3000, debug=True)
```

### VS Code Settings
```json
{
    "files.exclude": {
        "**/__pycache__": true,
        "**/.pytest_cache": true
    }
}
```

## 🔮 Future Enhancements

- [ ] **Calculator 4**: Matrix operations with NumPy
- [ ] **Calculator 5**: Trigonometric calculations
- [ ] **API Documentation**: Swagger/OpenAPI integration
- [ ] **Database Integration**: Store calculation history
- [ ] **Authentication**: JWT token-based auth
- [ ] **Rate Limiting**: Request throttling
- [ ] **Docker**: Containerization support
- [ ] **CI/CD**: GitHub Actions pipeline
- [ ] **Logging**: Comprehensive logging system
- [ ] **Metrics**: Performance monitoring

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/Calculator4`)
3. Write tests for new features
4. Ensure all tests pass (`pytest`)
5. Commit changes (`git commit -m 'Add Calculator 4'`)
6. Push to branch (`git push origin feature/Calculator4`)
7. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create GitHub issue with detailed information
- Include request/response examples
- Provide error messages and stack traces
- Specify Python and NumPy versions

## 🏆 Acknowledgments

- Flask framework and community
- NumPy scientific computing library
- pytest testing framework
- Clean Architecture principles by Robert C. Martin
