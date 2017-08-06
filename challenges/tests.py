from django.test import TestCase

from challenges.models import Challenge


class ChallengeModelTest(TestCase):
    def test_str(self):
        challenge = Challenge()
        challenge.title = 'Title'
        self.assertEqual(str(challenge), 'Title')
