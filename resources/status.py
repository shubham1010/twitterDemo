from datetime import datetime
from flask import Response, request
from database.models import Status, User, Comments
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, InternalServerError, \
DeletingStatusError, UserNotExistsError


class CreateStatus(Resource):
  @jwt_required
  def post(self):
    try:
      user_id = get_jwt_identity()
      body = request.get_json()
      user = User.objects.get(id=user_id)
      status = Status(**body, added_by=user, time=str(datetime.now()))
      status.save()
      user.update(push__status=status)
      user.save()
      id = status.id
      return {'message':'Status is successfully uploaded', 'id': str(id)}, 200
    except InvalidQueryError:
      raise SchemaValidationError
    except (FieldDoesNotExist, ValidationError):    
      raise SchemaValidationError
    except Exception as e:
      raise InternalServerError

class GetUserStatus(Resource):
  @jwt_required
  def get(self):
    try:
      user_id = get_jwt_identity()
      status = Status.objects.get(added_by=user_id).to_json()
     
      return Response(status, mimetype="application/json", status=200)

    except DoesNotExist:
      raise UserNotExistsError
    except Exception:
      raise InternalServerError


class DeleteStatus(Resource):

  @jwt_required
  def delete(self, id):
    try:
      user_id = get_jwt_identity()
      status = Status.objects.get(id=id, added_by=user_id)
      status.delete()
      return {'message':'Your status is successfully deleted'}, 200
    except DoesNotExist:
      raise DeletingStatusError
    except Exception:
      raise InternalServerError
