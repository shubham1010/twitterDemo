from datetime import datetime

from flask import Response, request
from database.models import Likes, Status, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, InternalServerError, \
StatusNotExistsError, DeletingCommentError


class Like(Resource):
  @jwt_required
  def post(self, id): # status id
    try:
      user_id = get_jwt_identity()
      user = User.objects.get(id=user_id)
      status = Status.objects.get(id=id)
      like = Likes(added_by=user, statusid=id, time=str(datetime.now()))
      like.save()
      status.update(push__likes=like)
      status.save()
      id = status.id
      return {'message':'Your like this status', 'id': str(id)}, 200
    except (FieldDoesNotExist, ValidationError):
      raise SchemaValidationError
    except DoesNotExist:
      raise StatusNotExistsError
    except Exception as e:
      raise InternalServerError

  @jwt_required
  def delete(self, id): # like id
    try:
      user_id = get_jwt_identity()
      like = Likes.objects.get(id=id, added_by=user_id)
      like.delete()
      return {'message':'You Dislike this status'}, 200
    except DoesNotExist:
      raise DeletingCommentError
    except Exception:
      raise InternalServerError
