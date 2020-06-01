from .auth import SignupApi, LoginApi
from .status import CreateStatus, DeleteStatus, GetUserStatus
from .comments import AddComment, DeleteComment
from .users import UserInfo
from .follow import Follow
from .likes import Like

def initialize_routes(api):

  api.add_resource(UserInfo, '/api/myinfo')
  api.add_resource(Follow, '/api/follow/<id>')

  api.add_resource(SignupApi, '/api/auth/signup')
  api.add_resource(LoginApi, '/api/auth/login')

  api.add_resource(CreateStatus, '/api/createstatus')
  api.add_resource(GetUserStatus, '/api/status')
  api.add_resource(DeleteStatus, '/api/deletestatus/<id>')

  api.add_resource(AddComment, '/api/addcomment/<id>') # status id
  api.add_resource(DeleteComment, '/api/deletecomment/<id>')#comment id

  api.add_resource(Like, '/api/like/<id>')
