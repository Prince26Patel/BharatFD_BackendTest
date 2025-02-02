# assignment - FAQ API

This project provides an API for managing and querying FAQs (Frequently Asked Questions). It supports multilingual capabilities (English, Hindi, and Bengali).

## Table of Contents

- [Installation](#installation)
- [API Usage](#api-usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation

Follow the steps below to set up the development environment and run the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com//assignment.git
   cd BharatFD_backend_test
   cd assignment
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**

   For macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

   For Windows:
   ```bash
   .venv\Scripts\activate
   ```

4. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```bash
   python manage.py runserver
   ```

   Your application should now be running locally at `http://127.0.0.1:8000`.

## API Usage

The project exposes a simple API to retrieve and manage FAQs. You can access the following endpoints:

### Available Endpoints

- `GET /api/faqs/`: Fetch the list of FAQs in the default language (English).
- `GET /api/faqs/?lang=hi`: Fetch the list of FAQs in Hindi.
- `GET /api/faqs/?lang=bn`: Fetch the list of FAQs in Bengali.
- `POST /api/faqs/`: Create a new FAQ entry.
- `PUT /api/faqs/{id}/`: Update an existing FAQ entry.
- `DELETE /api/faqs/{id}/`: Delete an FAQ entry.

### API Examples

**Fetch FAQ List (English)**  
```bash
curl http://127.0.0.1:8000/api/faqs/
```

**Fetch FAQ List (Hindi)**  
```bash
curl http://127.0.0.1:8000/api/faqs/?lang=hi
```

**Fetch FAQ List (Bengali)**  
```bash
curl http://127.0.0.1:8000/api/faqs/?lang=bn
```

**Create a New FAQ**  
```bash
curl -X POST http://127.0.0.1:8000/api/faqs/ -H "Content-Type: application/json" -d '{"question": "What is Django?", "answer": "Django is a Python web framework."}'
```

**Update an Existing FAQ**  
```bash
curl -X PUT http://127.0.0.1:8000/api/faqs/1/ -H "Content-Type: application/json" -d '{"question": "Updated question", "answer": "Updated answer."}'
```

**Delete an FAQ**  
```bash
curl -X DELETE http://127.0.0.1:8000/api/faqs/1/
```

## Testing

To run tests for the project:

1. Ensure the virtual environment is activated.
2. Run the following command to execute tests:
   ```bash
   python manage.py test
   ```

The tests for the project are located in the `tests.py` file, and running the above command will execute all tests.

## Contributing

We welcome contributions to this project! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Clone your forked repository locally.
3. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
4. Make your changes and commit them:
   ```bash
   git commit -am 'Add feature description'
   ```
5. Push the branch:
   ```bash
   git push origin feature-name
   ```
6. Create a pull request from your branch to the main repository.

Please ensure all tests pass before submitting your pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

