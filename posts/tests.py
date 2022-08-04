# TestCase allows us to mock queries to the database
from django.test import TestCase
from django.urls import reverse
from .models import Post


class PostTests(TestCase):
  @classmethod
  def setUpTestData(cls) -> None:
    cls.post = Post.objects.create(text='This is a test!')

  def test_model_content(self):
    self.assertEqual(self.post.text, 'This is a test!')

  def test_url_at_correct_location(self):
    response = self.client.get('/posts/')
    self.assertEqual(response.status_code, 200)
  
  def test_homepage(self):
    response = self.client.get(reverse('posts'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'posts/posts.html')
    self.assertContains(response, 'This is a test!')
  