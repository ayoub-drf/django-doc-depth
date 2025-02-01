from django.test import TestCase
from .models import Animal

# Run all test cases across all apps
# python3 manage.py test

# Run all test cases inside the new_tests_1 app
# python3 manage.py test new_tests_1

# Run all test cases within a specific path
# python3 manage.py test path/to/tests

# Run all test cases inside the new_tests_1/tests
# python3 manage.py test new_tests_1.tests

# Run all test cases inside the AnimalTestCase class
# python3 manage.py test new_tests_1.tests.AnimalTestCase

# Run a test case function within a specific test class
# python3 manage.py test new_tests_1.tests.AnimalTestCase.test_animals_can_speak

# Run all test cases within this regular expression
# python3 manage.py test --pattern="test*.py"

class AnimalTestCase(TestCase):

    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")

        self.assertEqual(lion.speak(), "The lion says roar")
        self.assertEqual(cat.speak(), "The cat says meow")
