from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from polls.models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        future_question = Question(pub_date=timezone.now() + timedelta(days=30))
        self.assertFalse(future_question.was_published_recently())

    def test_was_published_recently_with_recent_question(self):
        recent_question = Question(pub_date=timezone.now() - timedelta(hours=1))
        self.assertTrue(recent_question.was_published_recently())
