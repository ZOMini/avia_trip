# import json

from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from trip.models import Company

User = get_user_model()

class Test_API(APITestCase):
    def setUp(self):
        self.user_a = User.objects.create_user(username='zomini',first_name='vit', last_name='pir', password='qwerasdf1',is_staff=True)
        self.token = Token.objects.create(user=self.user_a)
        # print(self.token.key)
        self.client = APIClient(enforce_csrf_checks=True)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
            
    def test_company(self):
        """ Test company (get,list,post,update,delete) response data & status """
        # ----post request----
        response = self.client.post('/api/v1/company/', {'name': 'UralAir'}, format='json')
        # print(f'-------{response.status_code}')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, {'id': 1, 'name': 'UralAir'})
        # ----get request----
        response = self.client.get('/api/v1/company/1/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'id': 1, 'name': 'UralAir'})
        # ----list request----
        self.client.post('/api/v1/company/', {'name': 'UralAir_2'}, format='json')
        response = self.client.get('/api/v1/company/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{"id": 1, "name": "UralAir"}, {"id": 2, "name": "UralAir_2"}])
        # print(json.dumps( response.data))
        # ----update request----
        response = self.client.put('/api/v1/company/1/', {'name': 'UralAir_3'}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'id': 1, 'name': 'UralAir_3'})
        # ----delete request----
        response = self.client.delete('/api/v1/company/1/', format='json')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(Company.objects.all()), 1)

