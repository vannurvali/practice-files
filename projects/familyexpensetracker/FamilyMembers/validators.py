from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size

    if filesize < 104857:
        raise ValidationError("The maximum file size that can be uploaded is 10kb")
    elif filesize > 100*1024:
        raise ValidationError("The maximum file size that can be uploaded is 100kb")
    else:
        return value