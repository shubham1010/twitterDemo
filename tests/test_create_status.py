import json

from tests.BaseCase import BaseCase

class TestUserLogin(BaseCase):

  def test_successful_login(self):
    # Given
    email = "shubhamjagdhane1010@gmail.com"
    password = "mycoolpassword"
    name = "Shubham Jagdhane"
    user_payload = json.dumps({
        "email": email,
        "password": password,
        "name": name
    })

    self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
    response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=user_payload)
    login_token = response.json['token']

    status_payload = {
      "image_url":"Beatiful", "caption":"Awesome"
    }
    # When
    response = self.app.post('/api/createstatus',
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
        data=json.dumps(status_payload))

    # Then
    self.assertEqual(str, type(response.json['id']))
    self.assertEqual(200, response.status_code)
