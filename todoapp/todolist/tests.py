from django.test import TestCase
from . models import Category, TodoList
# Create your tests here.

class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='Important')