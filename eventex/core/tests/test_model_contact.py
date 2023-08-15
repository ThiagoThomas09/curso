from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact

class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Michael Scott',
            slug='michael-scott',
            photo='https://miro.medium.com/v2/resize:fit:1396/1*njwXqsShWvK81ANQCMBevw.jpeg'
        )

    def test_email(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='michael@scott.net'
        )

        self.assertTrue(Contact.objects.exists())
    
    def test_phone(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE,
            value='21-996186180'
        )
    
    def test_choices(self):
        """Contact kind should be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)
    
    def test_str(self):
        contact = Contact(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='michael@scott.net'
        )
        self.assertEqual('michael@scott.net', str(contact))