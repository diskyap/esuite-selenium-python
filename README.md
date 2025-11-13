# esuite-selenium-python
This is a Python Selenium pytest framework designed for automated testing of web applications. Frameworks provide a structured approach to software development, and in the context of testing, they offer a systematic way to organize, execute, and maintain tests.

# 🚀 Quick Start
### 1️⃣ Clone the Repository
```
 git clone https://github.com/diskyap/esuite-selenium-python.git
```
### 2️⃣ Install Dependencies 
```
pip install -r requirements.txt
```

## 🧪 Running Tests
### ▶️ Execute All Tests

```bash
pytest
```

### Execute with reporting allure report
```
pytest --alluredir=reports/allure-results
```

## 📂 Project Architecture
```
ESUITE-SELENIUM-PYTHON/ # The main project directory.
├── 📂 pages/               # Stores all Page Object Models (POMs). The core of code separation.
│   ├── __init__.py         # Marks the 'pages' directory as a Python package, allowing its modules to be imported.
│   ├── base.page.py        # The parent class (BasePage) with reusable Selenium methods (click, get_element, waits).
│   ├── companies.page.py   # Page Object specific to the Company Management page.
│   └── sign_in.page.py     # Page Object specific to the Login/Sign In page.
│
├── 📂 reports/             # This folder should contain test execution results (like Allure or HTML reports).
│   └── 📂 allure-results    # # Stores test reporting output (e.g., Allure data or HTML reports).
|
├── 📂 tests/               # This folder contains all the Pytest test case files to be executed.
│   ├── __init__.py          # # Marks the 'tests' directory as a Python package.
│   ├── test.companies.py    # # Test case file containing scenarios for Company Management functionality.
│   └── test_sign_in.py      # # Test case file containing scenarios for the Sign In/Login functionality.
│ 
└── 📄 conftest.py          # # The primary Pytest configuration file. It holds all reusable Fixtures (setup/teardown) shared across the project (e.g., WebDriver initialization).
└── 📄 requirements.txt     # # Lists all external Python libraries required for the project (e.g., selenium, pytest, faker, webdriver-manager). Used for dependency installation (pip install -r requirements.txt).
```