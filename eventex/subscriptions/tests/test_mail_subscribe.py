from django.core import mail
from django.test import TestCase



class SubscribePostValid(TestCase):
    def setUp(self):
        """Valid Post should redirect to /inscricao/"""
        data = dict(name='Thiago Assis', cpf='12345678901', 
                    email='thiagoassis@instruct.com.br', phone='61999999999')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]


    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    
    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)
    

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'thiagoassis@instruct.com.br']

        self.assertEqual(expect, self.email.to)


    def test_subscription_email_body(self):
        contents = [
            'Thiago Assis',
            '12345678901',
            'thiagoassis@instruct.com.br',
            '61999999999',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content,self.email.body)
