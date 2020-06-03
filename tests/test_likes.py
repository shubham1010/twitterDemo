import json

from tests.BaseCase import BaseCase

class TestUserLike(BaseCase):

  def test_like_a_post_by_self(self):
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
    response = self.app.post('/api/createstatus',
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
        data=json.dumps(status_payload))

    # When
    statusid = response.json['id']
    response = self.app.post('/api/like/'+statusid,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"})

    # Then
    self.assertEqual('You liked this status', response.json['message'])
    self.assertEqual(200, response.status_code)

  def test_like_a_post_by_other(self):
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
    response = self.app.post('/api/createstatus',
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
        data=json.dumps(status_payload))


    statusid = response.json['id']

    # When
    email = "abc@gmail.com"
    password = "1234d"
    name = "Some User"
    user_payload = json.dumps({
        "email": email,
        "password": password,
        "name": name
    })

    self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
    response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=user_payload)
    login_token = response.json['token']


    response = self.app.post('/api/like/'+statusid,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"})

    # Then
    self.assertEqual('You liked this status', response.json['message'])
    self.assertEqual(200, response.status_code)

  def test_like_a_same_post_again_other(self):
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
    response = self.app.post('/api/createstatus',
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
        data=json.dumps(status_payload))


    statusid = response.json['id']

    # Other User

    email = "abc@gmail.com"
    password = "1234d"
    name = "Some User"
    user_payload = json.dumps({
        "email": email,
        "password": password,
        "name": name
    })

    self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
    response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=user_payload)
    login_token = response.json['token']


    response = self.app.post('/api/like/'+statusid,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"})

    # When (2nd liking the same post)
    response = self.app.post('/api/like/'+statusid,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"})

    # Then
    self.assertEqual('You have already liked this status', response.json['message'])
    self.assertEqual(406, response.status_code)

