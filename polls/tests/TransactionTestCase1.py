from django.test import TransactionTestCase
from django.utils import timezone
from polls.models import Question


class QuestionTransactionTest(TransactionTestCase):

    def test_create_question(self):
        q = Question.objects.create(
            question_text="Test Question",
            pub_date=timezone.now()
        )

        self.assertEqual(Question.objects.count(), 1)
        self.assertEqual(q.question_text, "Test Question")
