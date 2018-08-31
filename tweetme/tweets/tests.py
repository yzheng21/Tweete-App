from django.test import TestCase
from .models import Tweet
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.urls import reverse
# Create your tests here.

class TweetModelTestCase(TestCase):
    def setUp(self):
        some_random_user = User.objects.create(username = 'jmakdf33333')

    def test_tweet_item(self):
        obj = Tweet.objects.create(
            user=User.objects.first(),
            content='some random content',
        )
        self.assertTrue(obj.content == 'some random content')
        self.assertTrue(obj.id == 1)
        self.assertEqual(obj.id, 1)
        absolute_url = reverse('tweet:detail',kwargs={'pk':1})
        self.assertEqual(obj.get_absolute_url(),absolute_url)

    def test_tweet_url(self):
        obj = Tweet.objects.create(
            user=User.objects.first(),
            content='some random content',
        )
        absolute_url = reverse('tweet:detail', kwargs={'pk': obj.pk})
        self.assertEqual(obj.get_absolute_url(), absolute_url)