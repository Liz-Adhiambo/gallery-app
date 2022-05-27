from django.test import TestCase
from .models import Image

# Create your tests here.
class ImageTestClass(TestCase):
    # Set up Method
    def setUp(self):

        self.image = Image(name='image test',photo='image', description='my test')
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))
    # Testing Save Method
    def test_save_method(self):
        self.image.save_image()
        images  = Image.objects.all()
        self.assertTrue(len(images)>0)

    def tearDown(self):
        self.image.delete_image()
