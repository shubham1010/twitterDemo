from datetime import datetime

from flask import Response, request
from database.models import Comments, Status, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, InternalServerError, \
StatusNotExistsError, DeletingCommentError


class AddComment(Resource):
  @jwt_required
  def post(self, id): # status id
    try:
      user_id = get_jwt_identity()
      body = request.get_json()
      user = User.objects.get(id=user_id)
      status = Status.objects.get(id=id)
      comment = Comments(**body, added_by=user, statusid=id, time=str(datetime.now()))
      comment.save()
      status.update(push__comments=comment)
      status.save()
      id = status.id
      return {'message':'Your comment is succssfully added', 'id': str(id)}, 200
    except (FieldDoesNotExist, ValidationError):
      raise SchemaValidationError
    except DoesNotExist:
      raise StatusNotExistsError
    except Exception as e:
      raise InternalServerError


class DeleteComment(Resource):
  @jwt_required
  def delete(self, id): # comment id
    try:
      user_id = get_jwt_identity()
      comment = Comments.objects.get(id=id, added_by=user_id)
      comment.delete()
      return {'message':'Your comment is successfully deleted'}, 200
    except DoesNotExist:
      raise DeletingCommentError
    except Exception:
      raise InternalServerError
