from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeGet(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')
    
    
    def test_get(self):
        """Get /inscricao/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)


    def test_template(self):
        """Must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    
    def test_html(self):
        """Html must contain input tags"""
        tags = (('<form',1),
                ('<input', 6),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1))
        
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


    def teste_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')


    def test_has_form(self):
        """Context mus have subscription form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)



class SubscribePostValid(TestCase):
    def setUp(self):
        """Valid Post should redirect to /inscricao/"""
        data = dict(name='Thiago Assis', cpf='12345678901', 
                    email='thiagoassis@instruct.com.br', phone='61999999999')
        self.resp = self.client.post('/inscricao/', data)



    def test_post(self):
        self.assertEqual(302, self.resp.status_code)


    def test_send_subscribe_email(self):
        self.assertEqual(1,len(mail.outbox))

 
class SubsribePostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post('/inscricao/', {})
    
    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.resp.status_code)
    
    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

class SubscribeSuccessMessage(TestCase):
    def test_message(self):
        data = dict(name='Thiago Assis', cpf='12345678901', 
                          email='thiagoassis@instruct.com.br', phone='61999999999')

        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, 'Inscrição realizada com sucesso')
    
        