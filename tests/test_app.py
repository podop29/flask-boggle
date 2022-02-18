from app import app
from flask import session
from unittest import TestCase


class appTestCase(TestCase):
    def test_home(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn("<tr>",html)


    def test_check_word(self):
        with app.test_client() as client:
            res = client.post('/check-word', data={'word': 'hello'})
            self.assertEqual(res.status_code, 405)


 



            

            
