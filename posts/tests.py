from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Posts
# Create your tests here.

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()
        test_post = Posts.objects.create(title='Test Post', body= 'Test Post Body', author=testuser1)
        test_post.save()

    def test_blog_content(self):
        post = Posts.objects.get(id=1)
        expected_author= f'{post.author}'
        expected_title= f'{post.title}'
        expected_body= f'{post.body}'
        self.assertEqual(expected_author, 'testuser1')
        self.assertEqual(expected_title, 'Test Post')
        self.assertEqual(expected_body, 'Test Post Body')


