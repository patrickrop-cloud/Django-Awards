from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile,Project

# Create your tests here.

#setup method
class ProjectTestclass(TestCase):
    def setUp(self):
        self.projects = Project(title = 'mytitle', description='description',screenshot1='s1',screenshot2='s2',screenshot3='s3',link='link')

#Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.projects,Project))