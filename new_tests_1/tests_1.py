from django.test import (
    Client, 
    TestCase, 
    SimpleTestCase,
    TransactionTestCase,
    LiveServerTestCase,
    override_settings,
    modify_settings,
    tag,
)
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from django.urls import reverse
from .utils import transaction_view
from .models import Animal
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from django.test.utils import isolate_apps
from django.db import models
from django.apps import apps
from django.template.loader import render_to_string
options = Options()
options.add_argument("-profile")
options.add_argument("/home/x/snap/firefox/common/.mozilla/firefox/exnmk0a8.x") 


from io import StringIO
from django.core.management import call_command

class CommandTestCase(TestCase):
    # @skipIfDBFeature("supports_transactions") # skip this if the db supports_transactions
    def test_command_output(self):
        command_output = StringIO()
        call_command("my_command", "james", stdout=command_output)
        self.assertIn('Hell james', command_output.getvalue())

# Testing asynchronous code
class AsynchronousTestCase(TestCase):
    async def test_sync_view(self):
        res = await self.async_client.get('/index2/')
        print(res.json())

class MyModelTests(TestCase):
    @isolate_apps("new_tests_1")
    def test_model_definition(self):
        class Animal(models.Model):
            name = models.CharField(max_length=100)
            sound = models.CharField(max_length=100)

        Animal.objects.create(name="x", sound="x")
        self.assertEqual(Animal.objects.count(), 1)

# @tag("slow", "core") #python manage.py test new_tests_1.tests_1.MyTestCaseExceptions --tag=fast --tag=core --exclude-tag=slow
class MyTestCaseExceptions(SimpleTestCase):
    @tag("fast")
    def test_fast(self): print("test_fast")

    @tag("slow")
    def test_slow(self): print("slow")

    @tag("slow", "core")
    def test_slow_but_core(self): print("test_slow_but_core")

    @tag("main")
    def test_value_error(self):
        # with self.assertRaisesMessage(ValueError, "==> invalid type for int()"):
        #     int("a")

        self.assertHTMLEqual(
            "<p>Hello <b>&#x27;world&#x27;!</p>",
            """<p>
                Hello   <b>&#39;world&#39;! </b>
            </p>""",
        )

        with self.assertTemplateUsed(template_name="new_tests_1/index.html"):
            temp = render_to_string("new_tests_1/index.html")

        self.assertHTMLNotEqual(
            "<p>Hello <b>&#x7;world&#x27;!</p>",
            """<p>
                Hello world
            </p>""",
        )


        self.assertURLEqual("http://127.0.0.1:8000/", "http://127.0.0.1:8000/")


        temp = render_to_string("new_tests_1/index.html")

        self.assertNotInHTML("DocumentX", temp)
        self.assertInHTML("Document", temp)

        self.assertJSONEqual('{"name": "James"}', '{"name": "James"}', msg="Not equal")

        self.assertJSONNotEqual('{"name": "James"}', '{"name": "Dexter"}', msg="equal")



@override_settings(LOGIN_URL="/other/login/")
class LoginTestCaseSetting(TestCase):

    # @override_settings(LOGIN_URL="/other/login/")
    def test_login(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)

class CustomLiveServerTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(options=options)
        cls.selenium.implicitly_wait(100)
        User.objects.create_superuser(username="x", password="x")

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get(f"{self.live_server_url}/admin/")
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys("x")
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys("x")
        self.selenium.find_element(By.XPATH, '//input[@value="Log in"]').click()

        WebDriverWait(self.selenium, 10).until(
            lambda driver: driver.find_element(By.TAG_NAME, "body")
        )   



    # def test_home_view(self):
    #     User.objects.create_user(username="x", password="x")
    #     client = Client()
    #     client.login(username="x", password="x")
    #     res = client.get("/")

    #     print(self.live_server_url)

    #     self.assertEqual(res.status_code, 200)

class CustomTransactionTestCase(TransactionTestCase): # used mostly for database transactions and flushes database after each test
    # databases = {"default", "other"} # multi dbs
    def test_create_animal(self):
        self.assertEqual(Animal.objects.count(), 0)
        transaction_view(name="cat", sound="meow")
        self.assertEqual(Animal.objects.count(), 1)
        self.assertEqual(Animal.objects.first().name, "cat")


class CustomSimpleTestCase(SimpleTestCase): # SimpleTestCase does not require database access
    def setUp(self):
        self.client = Client()

    def test_index1(self):
        res = self.client.get('/index1/')
        # print(res.json())
        # print(dir(res))

        print(res.headers)
        self.assertEqual(res.status_code, 200)
    

class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="x", password="x")
        self.client.login(username="x", password="x")

    def test_login(self):
        # self.client.logout()
        res = self.client.get('/')

        # print(res.json())
        # print(res.cookies)
        # session = res.client.session
        # session['name'] = "James"
        # print(session['name'])

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Hello world")


class Index1TestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def index1_test(self):
        res = self.client.get('/index1/')
        # print(res.json())
        # print(dir(res))

        print(res.headers)


        self.assertIs(res.resolver_match.func, index_1)
        self.assertEqual(res.resolver_match.func, index_1)
        self.assertEqual(res.status_code, 200)


class MyViewTestCase(TestCase):
    def setUp(self):
        self.client = Client(enforce_csrf_checks=True)
        res = self.client.get('/')
        self.csrftoken = res.cookies['csrftoken'].value

    def test_home_get(self):
        res = self.client.get('/')

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Hello world")

    def test_home_post(self):
        # file = SimpleUploadedFile(
        #     name="product.txt",
        #     content=b"hello world",
        #     content_type="text/plain"
        # )
        # res = self.client.post('/', {'file': file, 'name': "James",'age': 33, "csrfmiddlewaretoken": self.csrftoken})

        # with open("/home/x/Pictures/Screenshots/x.png", "rb+") as file:
            # print(file.read())
            # res = self.client.post('/', {'file': file, 'name': "James",'age': 33, "csrfmiddlewaretoken": self.csrftoken})


        img = BytesIO(b"\x89PNG\x01\x00\x01\x00\x00\x00\x00!\xf9\x04\x01\x00\x00\x00")
        img.name = "image.png"
        print(img)
        res = self.client.post('/', {'file': img, 'name': "James",'age': 33, "csrfmiddlewaretoken": self.csrftoken})

    
        # print("res.charset:", res.charset)
        # print("res.context:", res.context)
        # print("res.cookies:", res.cookies)
        # print("res.request:", res.request)
        # print("res.status_code:", res.status_code)
        # print("res.content:", res.content)

        self.assertRedirects(res, "/form_submitted/")