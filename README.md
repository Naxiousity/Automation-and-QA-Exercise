# 🧪 QA Automation Framework

Automated testing framework for [automationexercise.com](https://automationexercise.com), built using:

- ✅ **Pytest** for test structure
- 🌐 **Requests** for API testing
- 🖱️ **Selenium** for UI testing
- 🐳 **Docker** + **Selenium Grid** for browser execution
- ⚙️ **GitHub Actions** for CI/CD pipelines

---

## 📂 Project Structure

```
.
├── automation/
│   └── pages/               # Page Object Models (POM) for UI tests
├── tests/
│   ├── api/                 # API test cases
│   └── test_login.py        # UI test case: login flow
├── Dockerfile               # Test container setup
├── docker-compose.yml       # Runs Selenium and tests
├── requirements.txt         # Python dependencies
└── .github/
    └── workflows/
        └── tests.yml        # GitHub Actions workflow
```

---

## ▶️ How to Run Tests Locally

### 🧪 API Tests

```bash
pytest tests/api/
```

### 🖥️ UI Tests (requires ChromeDriver)

```bash
pytest tests/test_login.py
```

### 🐳 Run with Docker

```bash
docker-compose up --build
```

---

## 🔄 CI/CD with GitHub Actions

Tests run automatically when you push to the `master` branch.

The pipeline includes:
- ✅ API Tests
- ✅ UI Login Tests (Selenium with Docker)

You can find the workflow config in `.github/workflows/tests.yml`.

---

## ⚙️ Environment Variable

Used for Selenium inside Docker:

```env
SELENIUM_REMOTE_URL=http://selenium:4444/wd/hub
```

---

## 👨‍💻 Author

**[Your Name]**  
*QA Automation Engineer*