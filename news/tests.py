from django.test import TestCase

from news.models import Editor, Article, Tags

# Create your tests here.
class EditorTestClass(TestCase):

    # set up method
    def setUp(self):
        self.james = Editor(first_name='James', last_name='Muriuki', email='jamesmuriuki@gmail.com')

    # test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james, Editor))

    # test save method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)