import datetime
from urllib import response 

from django.test import TestCase
from django.urls.base import reverse
from django.utils import timezone
from .models import Question

# voy a testear Modelos y vista que es lo mas comun
class QuestionModelTexts(TestCase): # es una clase que viene del modulo test de django que nos permite difinir una bateria de tests
    # creamos un nombre descriptivo que sea facil de saber para que que el test 
    def test_was_published_recently_with_future_questions(self):
        """was_published_recently returs False for question whose pub_date in the future"""
        time = timezone.now() + datetime.timedelta(days= 30)
        future_question = Question(question_text="¿Quien es el mejor Course Director de Platzi?", pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)# assrtIs yo afimo que ele resultado es tal como que se debe 
    
    
    def test_was_published_recently_with_present_questions(self):
       """was_publishes_rencently retur True for question whose puub_date in the present""" 
       time = timezone.now() - datetime.timedelta(hours=23)
       present_question =  Question(question_text="¿Quien es el mejor Course Director en Platzi?", pub_date=time)
       self.assertIs(present_question.was_published_recently(), True)
        
    def test_was_published_recently_with_past_questions(self):
       """was_publishes_rencently retur True for question whose puub_date in the present""" 
       time = timezone.now() - datetime.timedelta(days=5)
       past_question =  Question(question_text="¿Quien es el mejor Course Director en Platzi?", pub_date=time)
       self.assertIs(past_question.was_published_recently(), False)   
    
    # def test_create_question_without_choices(self):
    #     """
    #     If the questions hasn't choices it is  deleted.
    #     """
    #     question =  Question.objects.create(question_text= "Quien el eso mejor CD de platzi",pub_date=timezone.now(), choices=0)
    #     if question.choices <= 1:
    #         question.delete()
    #         questions_count = len(Question.objects.all())
    #     self.assertEqual(questions_count, 0)

def create_question(question_text, days):
    """Create a question with the given "question_text", and published the given
    number of days ooset to now (negative for questions published in the past,
    positive for questions that have yet to be published) """
    
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexTests(TestCase):
    def test_no_question(self):
        """If no question exist, an appropiate message is displayed"""
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are avaliable.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
            
    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on the index page. 
        """
        create_question("Future question", days=30)
        response  = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
            
    def test_past_questions(self):
        """
        Questions with a pub_date in the past are displayed on the index page
        """
        question = create_question("Past question", days=-10)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])
        
    def test_future_question_and_past_questions(self):
        """
        Even if both past and future question exist, only past questions are displayed
        """
        past_question  = create_question("Past question", days=-30)
        future_question = create_question("Future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [past_question]
        )
    
    def test_two_past_question(self):
        """
        The questions index page may display multiple questions.
        """    
        past_question1 = create_question("Past question1", days=-30)
        past_question2 = create_question("Past question2", days=-40)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [past_question1,past_question2]
        )
    
    # def test_two_future_questions(self):
    #     """
    #     Two Question with pub_date in the future aren't displayed in the index page
    #     """
    #     future_question1 = create_question("Future question1", days= 30)
    #     future_question2 = create_question("Future question2", days= 40)
    #     response = self.client.get("polls:index")
    #     self.assertQuerysetEqual(response.context["latest_question_list"], [])    

class QuestionDetailViewTest(TestCase):
    
    def test_future_question(self):
        """
        The Detail view of the question with a pub_date in the future returns a 404 error not found 
        """
        future_question = create_question(question_text="Future question", days=30)
        url= reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        
    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past display the question's text
        """
        past_question = create_question(question_text="Past question", days=-30)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

class QuestionResultViewTest(TestCase):
    def test_no_question(self):
        """
        The result view of a question that doesn't exist 
        return a 404 errot not found
        """
        url = reverse("polls:results", args=(1,))
        response= self.client.get(url)
        self.assertEqual(response.status_code, 404)
        
    def test_future_question(self):
        """
        The result view of a question with a pub_date
        in the future return 404 error not found
        """
        
        future_question = create_question(question_text="Quien es el mejor CD de platzi", days=5)
        url = reverse("polls:results", args=(future_question.id, ))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
           
    def test_past_question(self):
        """
        The result view of a questioon with a pub_date in the past displays the question's text
        """
        past_question = create_question(question_text="Past question", days=-30)
        url= reverse("polls:results", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
         
        
        
             
