from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.core.models import Speaker

class SpeakerDetailGet(TestCase):
    def setUp(self):
        Speaker.objects.create(
            name='Michael Scott',
            slug='michael-scott',
            photo='https://miro.medium.com/v2/resize:fit:1396/1*njwXqsShWvK81ANQCMBevw.jpeg',
            website='http://hbn.link/scott-site',
            description ='Regional Manager'
        )
        self.resp = self.client.get(r('speaker_detail', slug='michael-scott'))

    def test_(self):
        """GET should return status 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')
    
    def test_html(self):
        contents = [
            'Michael Scott',
            'Regional Manager',
            'https://miro.medium.com/v2/resize:fit:1396/1*njwXqsShWvK81ANQCMBevw.jpeg',
            'http://hbn.link/scott-site',

        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected)

    def test_context(self):
        """Speaker must be in context"""
        speaker = self.resp.context['speaker']
        self.assertIsInstance(speaker, Speaker)

class SpeakerDetailNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get(r('speaker_detail', slug='not-found'))
        self.assertEqual(404, response.status_code)