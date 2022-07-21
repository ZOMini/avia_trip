from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from trip.models import Airport, Company, Pass_in_trip, Plane, Trip

User = get_user_model()

class Test_API(APITestCase):
    def setUp(self):
        self.user_a = User.objects.create_user(username='zomini',first_name='vit', last_name='pir', password='qwerasdf1',is_staff=True)
        self.token = Token.objects.create(user=self.user_a)
        # print(self.token.key)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
            
    def test_company(self):
        """ Test company (get,list,post,update,delete) response data & status """
        # ----post request----
        response = self.client.post('/api/v1/company/', {'name': 'UralAir'}, format='json')
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
        # ----update request----
        response = self.client.put('/api/v1/company/1/', {'name': 'UralAir_3'}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'id': 1, 'name': 'UralAir_3'})
        # ----delete request----
        response = self.client.delete('/api/v1/company/1/', format='json')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Company.objects.count(), 1)

    def test_plane(self):
        """ Test plane (get,list,post,update,delete) response data & status """
        # ----post request----
        response = self.client.post('/api/v1/plane/', {'name': 'TU-134',"number": 121212,"capacity": 150}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"id": 4, "name":"TU-134", "number": 121212, "ready": False, "capacity": 150})
        # ----get request----
        response = self.client.get('/api/v1/plane/4/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"id": 4, "name":"TU-134", "number": 121212, "ready": False, "capacity": 150})
        # ----list request----
        self.client.post('/api/v1/plane/', {'name': 'TU-154',"number": 2323232,"capacity": 175}, format='json')
        response = self.client.get('/api/v1/plane/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{'capacity': 150, 'id': 4, 'name': 'TU-134', 'number': 121212, 'ready': False},{'capacity': 175, 'id': 5, 'name': 'TU-154', 'number': 2323232, 'ready': False}])
        # ----update request----
        response = self.client.put('/api/v1/plane/4/', {"id": 4, "name":"TU-134", "number": 777777, "ready": False, "capacity": 155}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"id": 4, "name":"TU-134", "number": 777777, "ready": False, "capacity": 155})
        # ----delete request----
        response = self.client.delete('/api/v1/plane/4/', format='json')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Plane.objects.count(), 1)

    def test_airport(self):
        """ Test airport (get,list,post,update,delete) response data & status """
        # ----post request----
        response = self.client.post('/api/v1/airport/', {"name": "Пулково-1(Санкт-Петербург)"}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'ap_time_zone': 'UTC', 'id': 1, 'name': 'Пулково-1(Санкт-Петербург)'})
        # ----get request----
        response = self.client.get('/api/v1/airport/1/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'ap_time_zone': 'UTC', 'id': 1, 'name': 'Пулково-1(Санкт-Петербург)'})
        # ----list request----
        self.client.post('/api/v1/airport/', {'name': "Шереметьево(Москва)"}, format='json')
        response = self.client.get('/api/v1/airport/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{'ap_time_zone': 'UTC', 'id': 1, 'name': 'Пулково-1(Санкт-Петербург)'},{'ap_time_zone': 'UTC', 'id': 2, 'name': 'Шереметьево(Москва)'}])
        # ----update request----
        response = self.client.put('/api/v1/airport/1/', {"name": "Пулково-2(Санкт-Петербург)"}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'ap_time_zone': 'UTC', 'id': 1, 'name': 'Пулково-2(Санкт-Петербург)'})
        # ----delete request----
        response = self.client.delete('/api/v1/airport/1/', format='json')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Airport.objects.count(), 1)

    def test_post_unauth(self):
        """ Test write operation - unauth """
        self.client.credentials() # <- unauth
        response = self.client.post('/api/v1/airport/', {"name": "Пулково-1(Санкт-Петербург)"}, format='json')
        self.assertEqual(response.status_code, 401)
        response = self.client.put('/api/v1/airport/1/', {"name": "Пулково-2(Санкт-Петербург)"}, format='json')
        self.assertEqual(response.status_code, 401)
        response = self.client.delete('/api/v1/airport/1/', format='json')
        self.assertEqual(response.status_code, 401)
        response = self.client.post('/api/v1/plane/', {'name': 'TU-134',"number": 121212,"capacity": 150}, format='json')
        self.assertEqual(response.status_code, 401)
        response = self.client.put('/api/v1/airport/1/', {"name": "Пулково-2(Санкт-Петербург)"}, format='json')
        self.assertEqual(response.status_code, 401)
        response = self.client.delete('/api/v1/airport/1/', format='json')
        self.assertEqual(response.status_code, 401)
        response = self.client.post('/api/v1/company/', {'name': 'UralAir'}, format='json')
        self.assertEqual(response.status_code, 401)
        response = self.client.put('/api/v1/company/1/', {'name': 'UralAir_3'}, format='json')
        self.assertEqual(response.status_code, 401)
        response = self.client.delete('/api/v1/company/1/', format='json')
        self.assertEqual(response.status_code, 401)

    def test_get_unauth(self):
        """ Test read(get,list) operation - unauth """
        self.client.post('/api/v1/company/', {'name': 'UralAir'}, format='json')
        self.client.post('/api/v1/company/', {'name': 'UralAir_2'}, format='json')
        self.client.post('/api/v1/plane/', {'name': 'TU-134',"number": 121212,"capacity": 150}, format='json')
        self.client.post('/api/v1/plane/', {'name': 'TU-154',"number": 2323232,"capacity": 175}, format='json')
        self.client.post('/api/v1/airport/', {"name": "Пулково-1(Санкт-Петербург)"}, format='json')
        self.client.post('/api/v1/airport/', {'name': "Шереметьево(Москва)"}, format='json')

        self.client.credentials() # <- unauth

        response = self.client.get('/api/v1/company/3/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'id': 3, 'name': 'UralAir'})
        response = self.client.get('/api/v1/company/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{"id": 3, "name": "UralAir"}, {"id": 4, "name": "UralAir_2"}])
        
        response = self.client.get('/api/v1/plane/1/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"id": 1, "name":"TU-134", "number": 121212, "ready": False, "capacity": 150})
        response = self.client.get('/api/v1/plane/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{'capacity': 150, 'id': 1, 'name': 'TU-134', 'number': 121212, 'ready': False},{'capacity': 175, 'id': 2, 'name': 'TU-154', 'number': 2323232, 'ready': False}])
        
        response = self.client.get('/api/v1/airport/3/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'ap_time_zone': 'UTC', 'id': 3, 'name': 'Пулково-1(Санкт-Петербург)'})
        response = self.client.get('/api/v1/airport/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{'ap_time_zone': 'UTC', 'id': 3, 'name': 'Пулково-1(Санкт-Петербург)'},{'ap_time_zone': 'UTC', 'id': 4, 'name': 'Шереметьево(Москва)'}])

    def test_trip(self):
        """ Test trip (get,list,post,update,delete) response data & status """
        # ----post request----
        self.client.post('/api/v1/company/', {'name': 'UralAir'}, format='json')
        self.client.post('/api/v1/plane/', {'name': 'TU-134',"number": 121212,"capacity": 150}, format='json')
        self.client.post('/api/v1/airport/', {"name": "Пулково-1(Санкт-Петербург)"}, format='json')
        self.client.post('/api/v1/airport/', {'name': "Шереметьево(Москва)"}, format='json')
        response = self.client.post('/api/v1/trip/', {"time_out": "2022-07-23T05:30:00Z","time_in": "2022-07-23T06:00:00Z","company": 6,"plane": 6,"airport_from": 7,"airport_to": 8}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"id": 2,"time_out": "2022-07-23T05:30:00Z","time_in": "2022-07-23T06:00:00Z","company": 6,"plane": 6,"airport_from": 7,"airport_to": 8})
        # ----get request----
        response = self.client.get('/api/v1/trip/2/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"id": 2,"company": "UralAir","plane": "TU-134","airport_from": "Пулково-1(Санкт-Петербург)","airport_to": "Шереметьево(Москва)","time_out": "2022-07-23T05:30:00Z","time_in": "2022-07-23T06:00:00Z"})
        # ----list request----
        self.client.post('/api/v1/trip/', {"time_out": "2022-07-23T06:30:00Z","time_in": "2022-07-23T07:00:00Z","company": 6,"plane": 6,"airport_from": 7,"airport_to": 8}, format='json')
        response = self.client.get('/api/v1/trip/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(type(response.json()), type([]))
        # ----update request----
        response = self.client.put('/api/v1/trip/2/', {"time_out": "2022-07-23T07:30:00Z","time_in": "2022-07-23T08:00:00Z","company": 6,"plane": 6,"airport_from": 7,"airport_to": 8}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"id":2,"time_out": "2022-07-23T07:30:00Z","time_in": "2022-07-23T08:00:00Z","company": 6,"plane": 6,"airport_from": 7,"airport_to": 8})
        # ----delete request----
        response = self.client.delete('/api/v1/trip/2/', format='json')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Trip.objects.count(), 1)

    def test_pass_in_trip(self):
        """ Test pass_in_trip (get,list,post,update,delete) response data & status """
        # ----post request----
        self.client.post('/api/v1/company/', {'name': 'UralAir'}, format='json')
        self.client.post('/api/v1/plane/', {'name': 'TU-134',"number": 121212,"capacity": 150}, format='json')
        self.client.post('/api/v1/airport/', {"name": "Пулково-1(Санкт-Петербург)"}, format='json')
        self.client.post('/api/v1/airport/', {'name': "Шереметьево(Москва)"}, format='json')
        self.client.post('/api/v1/trip/', {"time_out": "2022-07-23T05:30:00Z","time_in": "2022-07-23T06:00:00Z","company": 5,"plane": 3,"airport_from": 5,"airport_to": 6}, format='json')
        response = self.client.post('/api/v1/pass_in_trip/', {"passenger": 4,"trip": 1,"place": "145"}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"id":1,"passenger": 4,"trip": 1,"place": 145})
        # ----get request----
        response = self.client.get('/api/v1/pass_in_trip/1/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'id': 1, 'passenger': 'zomini', 'place': 145,'trip': 'id: 1, по маршруту: Пулково-1(Санкт-Петербург) - ''Шереметьево(Москва), вылет 2022-07-23 05:30:00+00:00, прибытие ''2022-07-23 06:00:00+00:00'})
        # ----list request----
        self.client.post('/api/v1/pass_in_trip/', {"passenger": 4,"trip": 1,"place": "140"}, format='json')
        response = self.client.get('/api/v1/pass_in_trip/', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(type(response.json()), type([]))
        # ----update request----
        response = self.client.put('/api/v1/pass_in_trip/1/', {"passenger": 4,"trip": "1","place": "142"}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'id': 1,"passenger": 4,"trip": 1,"place": 142})
        # ----delete request----
        response = self.client.delete('/api/v1/pass_in_trip/1/', format='json')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Pass_in_trip.objects.count(), 1)
