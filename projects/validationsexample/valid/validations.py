#validation for mobile number
import re  #regular expressions
from django.core.exceptions import ValidationError


def phone_validation(phone):
    pattern = '^\+91-[0-9]{10}$'
    match = re.match(pattern,phone)
    if match is None:
        raise ValidationError("your number should in the format +91-xxxxxxxxxx")
    else:
        return phone

def email_validation(email):
    if '@' in email:
        return email
    else:
        raise ValidationError('your email is not correct ')

def file_validation(file):
    if file.size > 50000 and file.size < 100000:     # >50kb and <100kb
        return file
    else:
        raise ValidationError('your file should be greter than 250kb')



# phone_validation('+91-9494251828')