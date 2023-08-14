from django.test import TestCase
from django.shortcuts import resolve_url as r

class HomeTest(TestCase):
    fixtures = ['keynotes.json']

    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)
    
    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')
    
    def test_subscription_link(self):
        expected = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.response, expected)
    
    def test_speakers(self):
        """Must show keynote speakers"""
        contents = [
            'href="{}"'.format(r('speaker_detail', slug='michael-scott')),
            'Michael Scott',
            'https://miro.medium.com/v2/resize:fit:1396/1*njwXqsShWvK81ANQCMBevw.jpeg',
            'href="{}"'.format(r('speaker_detail', slug='jim-halpert')),
            'Jim Halpert',
            'https://www.denofgeek.com/wp-content/uploads/2021/10/Jim-The-Office-John-Krasinski.jpg?fit=1200%2C675',
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)
        
    def test_speakers_link(self):
        expected = 'href="{}#speakers"'.format(r('home'))
        self.assertContains(self.response, expected)