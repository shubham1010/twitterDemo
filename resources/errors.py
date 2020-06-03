class InternalServerError(Exception):
  pass

class SchemaValidationError(Exception):
  pass

class DeletingStatusError(Exception):
  pass

class DeletingCommentError(Exception):
  pass

class StatusNotExistsError(Exception):
  pass

class UserNotExistsError(Exception):
  pass

class EmailAlreadyExistsError(Exception):
  pass

class UnauthorizedError(Exception):
  pass

class AlreadyLikedError(Exception):
  pass

errors = {
  "InternalServerError": {
    "message": "Something went wrong",
    "status": 500
  },
  "SchemaValidationError": {
    "message": "Request is missing required fields",
    "status": 400
  },
  "DeletingCommentError": {
    "message": "Deleting comment added by other is forbidden",
    "status": 403
  },
  "DeletingStatusError": {
    "message": "Deleting status added by other is forbidden",
    "status": 403
  },

  "StatusNotExistsError": {
    "message": "Status is not exist",
    "status": 400
  },

  "UserNotExistsError": {
    "message": "User is not exist",
    "status": 400
  },

  "EmailAlreadyExistsError": {
    "message": "User with given email address already exists",
    "status": 400
  },
  "UnauthorizedError": {
    "message": "Invalid username or password",
    "status": 401
  },

   "AlreadyLikedError": {
    "message": "You have already liked this status",
    "status": 406
  },
    "LikeNotError": {
    "message": "Liked id is not found in the records",
    "status": 400
  }

}
