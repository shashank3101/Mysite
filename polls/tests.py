import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question


class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

        def test_was_published_recently_with_old_question(self):

            time = timezone.now() - datetime.timedelta(days=30)
            old_question = Question(pub_date=time)
            self.assertIs(old_question.was_published_recently(), False)

        def test_was_published_recently_with_recent_question(self):

            time = timezone.now() - datetime.timedelta(hours=1)
            recent_question = Question(pub_date=time)
            self.assertIs(recent_question.was_published_recently(), True)

            class QuestionIndexDetailTests(TestCase):
                def test_detail_view_with_a_future_question(self):

                    future_question = create_question(question_text='Future question.', days=5)
                    url = reverse('polls:detail', args=(future_question.id,))
                    response = self.client.get(url)
                    self.assertEqual(response.status_code, 404)

                def test_detail_view_with_a_past_question(self):
                   
                    past_question = create_question(question_text='Past Question.', days=-5)
                    url = reverse('polls:detail', args=(past_question.id,))
                    response = self.client.get(url)
                    self.assertContains(response, past_question.question_text)