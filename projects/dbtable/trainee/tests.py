from django.test import TestCase

# Create your tests here.


class Test:
    def __init__(self):
        self.name = None

    def save(self):
        print("saving")

t = Test()
t.name = "palle"
t.save()