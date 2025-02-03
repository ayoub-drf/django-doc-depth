SECRET_KEY = "fake-key"

INSTALLED_APPS = [
    "django.contrib.contenttypes",  # Needed for models to work
    "django.contrib.auth",  # Required for user-related tests
    "tests",  # Your test app
    'new_tests_2',
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # Use SQLite for fast testing
        "NAME": ":memory:",  # In-memory DB (faster, resets after tests)
    }
}

# Use a fast password hasher for testing
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

# Set test runner (optional)
TEST_RUNNER = "django.test.runner.DiscoverRunner"
