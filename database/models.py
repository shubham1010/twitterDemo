from datetime import datetime
from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash


class Likes(db.Document):
  statusid = db.ReferenceField('Status')
  added_by = db.ReferenceField('User', unique_with='statusid')
  liked_at = db.DateTimeField(required=True)

class Comments(db.Document):
  comment = db.StringField(required=True)
  statusid = db.ReferenceField('Status')
  added_by = db.ReferenceField('User')
  commented_at = db.DateTimeField(required=True)

class Status(db.Document):
  image_url = db.StringField()
  caption = db.StringField()
  comments = db.ListField(db.ReferenceField('Comments', reverse_delete_rule=db.PULL))
  likes = db.ListField(db.ReferenceField('Likes', reverse_delete_rule=db.PULL))
  added_by = db.ReferenceField('User')
  uploaded_at = db.DateTimeField(required=True)

class User(db.Document):
  email = db.EmailField(required=True, unique=True)
  password = db.StringField(required=True, min_length=6)
  name = db.StringField(required=True)
  status = db.ListField(db.ReferenceField('Status', reverse_delete_rule=db.PULL))
  following = db.ListField(db.ReferenceField('User', reverse_delete_rule=db.PULL, unique=True))
  followers = db.ListField(db.ReferenceField('User', reverse_delete_rule=db.PULL, unique=True))
  created_at = db.DateTimeField(required=True)
  last_logged_in = db.DateTimeField(required=True)

  def hash_password(self):
    self.password = generate_password_hash(self.password).decode('utf8')

  def check_password(self, password):
    return check_password_hash(self.password, password)

User.register_delete_rule(Status, 'added_by', db.CASCADE)
User.register_delete_rule(Comments, 'added_by', db.CASCADE)
