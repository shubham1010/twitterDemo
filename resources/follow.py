from flask import Response, request
from database.models import Status, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import UserNotExistsError, InternalServerError


class Follow(Resource):
  @jwt_required
  def post(self, id):
    try:
      user_following_id = get_jwt_identity()
      userFollowing = User.objects.get(id=user_following_id)
      userFollower = User.objects.get(id=id)

      userFollowing.update(add_to_set__following = userFollower)
      userFollowing.save()

      userFollower.update(add_to_set__followers = userFollowing)
      userFollower.save()

      userFollowerName = str(userFollower['name'])
      msg = "You started following "+userFollowerName
      d = {}
      d['message'] = msg
      return d, 200
    except DoesNotExist:
      raise UserNotExistsError
    except Exception:
      raise InternalServerError
