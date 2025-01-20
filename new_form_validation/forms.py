from django.forms import (
    Form,
    ModelForm,
    forms,
    ValidationError,
    IntegerField,
    CharField,
    FileField,
    DecimalField,
    FloatField,
    Field
)
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
    DecimalValidator,
    FileExtensionValidator,
    MaxLengthValidator,
    EmailValidator,
    MinLengthValidator,
    URLValidator,
    RegexValidator,
    validate_email
)
from django.utils.translation import gettext_lazy as _

MyMaxValueValidator = MaxValueValidator(99, "num must be less then 100")
MyMinValueValidator = MinValueValidator(1, "num must be greater then 0")

def validate_num(value):    
    if value % 2 != 0:
        raise ValidationError("Not an even number")

class MultiEmailField(forms.Field):
    def to_python(self, value):
        """Normalize data to a list of strings."""
        # Return an empty list if no input was given.
        if not value:
            return []
        return value.split(",")

    def validate(self, value):
        """Check if value consists only of valid emails."""
        # Use the parent's handling of required fields, etc.
        super().validate(value)
        for email in value:
            validate_email(email)

class MyForm(Form):
    recipients = MultiEmailField()
    phone_number = CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^1\d{9,15}$', message='Enter a valid phone number.')]
    )
    num = IntegerField(validators=[MyMaxValueValidator, MyMinValueValidator, validate_num])
    name = CharField(
        max_length=20,
        error_messages={
            'required': 'Name is mandatory!',
            'max_length': 'Name cannot be longer than 20 characters.',
        }
    )
    username = CharField()
    password = CharField(min_length=6)
    confirm_password = CharField(min_length=6)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")
            self.add_error('password', "Passwords do not match")
            raise ValidationError(_('Passwords do not match. (%(password)s)'), params={'password': password}, code="invalid")
        
    def clean_username(self):
        username = self.cleaned_data['username']
        if " " in username:
            raise forms.ValidationError('Username should not contain spaces.')