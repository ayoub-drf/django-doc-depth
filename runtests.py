#!/usr/bin/env python

import os
import sys

try:
    import django
except ImportError as e:
    raise RuntimeError(
        "Django module not found, reference tests/README.rst for instructions."
    ) from e
else:
    from django.test.utils import get_runner
    from django.conf import settings

if __name__ == "__main__":
    os.environ["DJANGO_SETTINGS_MODULE"] = "tests.test_settings"
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["tests"]) # for the tests inside the tests folder
    # failures = test_runner.run_tests(["new_tests_2"]) # run tests inside this app
    sys.exit(bool(failures))