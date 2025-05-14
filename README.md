# 🛠️ CI/CD Demo Project

This is a simple Python project demonstrating Continuous Integration (CI) using GitHub Actions.  
It includes unit tests, code linting, and test coverage analysis.

---

## 📁 Project Structure

```
├── main.py             # Basic Python functions
├── tests/
│   └── test_basic.py   # Unit tests with pytest
├── .github/workflows/
│   └── python-ci.yml   # GitHub Actions CI pipeline
├── requirements.txt    # Required dependencies
├── .gitignore          # Ignored files and directories
└── README.md           # Project documentation
```

---

## 🔧 Features

- ✅ **Unit Testing** with `pytest`
- ✅ **Code Linting** with `flake8`
- ✅ **Coverage Reporting** with `coverage.py`
- ✅ **CI/CD** with GitHub Actions

---

## 🚀 Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/berkaybakac/cicd-demo.git
   cd cicd-demo
   ```

2. (Optional) Create and activate virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
---

## 🧪 Running Tests

To run the tests and view code coverage:

```bash
coverage run -m pytest
coverage report -m
```

Or simply:

```bash
pytest
```

---

## ⚙️ Continuous Integration (CI)

The CI pipeline runs automatically on every push via [GitHub Actions](https://github.com/features/actions):

```yaml
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run linting
        run: flake8 .
      - name: Run tests + coverage
        run: |
          coverage run -m pytest
          coverage report
```

---

## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License.
