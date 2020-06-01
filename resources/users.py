from flask import Response, request
from database.models import User, Status, Comments
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import UserNotExistsError, InternalServerError


class UserInfo(Resource):
  @jwt_required
  def get(self):
    try:
      user_id = get_jwt_identity()
      user = User.objects.get(id=user_id).to_json()

      return Response(user, mimetype="application/json", status=200)

    except DoesNotExist:
      raise UserNotExistsError
    except Exception:
      raise InternalServerError
