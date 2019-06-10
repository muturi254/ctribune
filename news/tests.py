from django.test import TestCase
import datetime as dt

from news.models import Editor, Article, Tags

# Create your tests here.
class EditorTestClass(TestCase):

    # set up method
    def setUp(self):
        self.james = Editor(first_name='James', last_name='Muriuki', email='jamesmuriuki@gmail.com')

    # teardewn to clean db after test
    def tearDown(self):
        Editor.objects.all().delete()

    # test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james, Editor))

    # test save method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)


class ArticleTestClass(TestCase):
    
    # set up method
    def setUp(self):
        self.james = Editor(first_name= 'James', last_name='Muriuki', email='jamesmuriuki@gmail.com')
        self.james.save_editor()

        # initialize tags
        self.new_tag = Tags(name='tetsting')
        self.new_tag.save()

        self.new_article = Article(title='Test Article', post='This is a random post', editor=self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Article.objects.all().delete()
        Editor.objects.all().delete()
        Tags.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, "%Y-%m-%d").date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date)==0)