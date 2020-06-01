import unittest
import json

from tests.BaseCase import BaseCase

class TestComments(BaseCase):

  def test_create_comment(self):
    # Given
    email = "shubhamjagdhane1010@gmail.com"
    password = "1010"
    name = "Shubham"
    user_payload = json.dumps({
        "email": email,
        "password": password,
        "name":name
    })

    response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
    user_id = response.json['id']
    response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=user_payload)
    login_token = response.json['token']

    status_payload = {
      "image_url":"URL String",
      "caption": "This is status caption"
    }
    response = self.app.post('/api/createstatus',
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
        data=json.dumps(status_payload))
    statusid = response.json['id']

    text = "Looking Great"
    comment_payload = {
      "comment": text
    }
    # When
    response = self.app.post('/api/addcomment/'+statusid,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"}, data=json.dumps(comment_payload)
    )

    # Then
    self.assertEqual(str,type(response.json['id']))
    self.assertEqual(200, response.status_code)

  def test_comment_if_status_not_exist(self):
    # Given
    email = "shubhamjagdhane1010@gmail.com"
    password = "1010"
    name = "Shubham"
    user_payload = json.dumps({
        "email": email,
        "password": password,
        "name":name
    })

    response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=user_payload)
    user_id = response.json['id']
    response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=user_payload)
    login_token = response.json['token']

    status_payload = {
      "image_url":"URL String",
      "caption": "This is status caption"
    }
    response = self.app.post('/api/createstatus',
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
        data=json.dumps(status_payload))
    statusid = response.json['id']
    statusid += '112344'

    text = "Looking Great"
    comment_payload = {
      "comment": text
    }
    # When
    response = self.app.post('/api/addcomment/'+statusid,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"}, data=json.dumps(comment_payload)
    )

    # Then
    self.assertEqual(str,type(response.json['message']))
    self.assertEqual(400, response.status_code)
