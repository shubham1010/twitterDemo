# Kind of Twitter Clone

This project is made for the kind of Twitter API.

## Getting Started

1. Clone the project.
2. cd twitterDemo
3. python3 -m pipenv install
4. Execute command python3 -m pipenv shell.
5. Execute command ./run.sh


### Prerequisites

```
python3
pip3
MongoDB

```

### Installing

1) python3:
For linux you can install from [Here](https://docs.python-guide.org/starting/install3/linux/)
For mac you can install from [Here](https://docs.python-guide.org/starting/install3/osx/)

2) pip3env:
For Ubuntu you can install from [Here](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/)
For mac you can install from [Here](https://evansdianga.com/install-pip-osx/)

3) MongoDB:
For linux you can install from [Here](https://docs.mongodb.com/manual/administration/install-on-linux/)
For mac you can install from [Here](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/)

## Running the tests

Execute command ./test.sh
You we see the server will running, then do ctrl+c to stop the server you will see the result of each test cases.

If you want to run a single test once a time, make sure that you are inside twitterDemo directory and then use command python3 -m unittest test/testname.py

### Break down into end to end tests
You can see the directory twitterDemo/test for all test cases.
You can see each file for more details, function name itself gives you idea about which test is for what purpose.

```
test_successful_signup: Check whether user is successfully going to signup or not.

test_creating_alread_existing_user: You cannot create account if the user is already exists.

test_signup_with_non_existing_field: If fields are missing then you can able to signup for user.

test_comment_if_status_not_exist: You cannot add comment for non-existing status/post.

and others.

```

### API

Here comes the main part.

```
[POST METHOD]
1) /api/auth/signup: 
This API is for creating/signing up the user.
Request Data=> 
{ "email":"shubhamjagdhane1010@gmail.com", "password":"1010", "name":"Shubham Jagdhane" }
Response=> If succeed you we get id of the created user otherwise you will get an appropriate error.
{ "id": "5ed4b501545ad540d4d57fe1" }

[POST METHOD]
2) /api/auth/login:
This API is for user login purpose.
Request Data=>
{ "email":"shubhamjagdhane1010@gmail.com", "password":"1010" }
Response=> If succeed you will receive token as follows otherwise you will get an error.
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1OTA5OTgyNzksIm5iZiI6MTU5MDk5ODI3OSwianRpIjoiMWVjZjIzMWUtNGNjMy00ZTY5LTk3MTAtZDY3Y2JhMDMwNmI4IiwiZXhwIjoxNTkxNjAzMDc5LCJpZGVudGl0eSI6IjVlZDRiNTAxNTQ1YWQ1NDBkNGQ1N2ZlMSIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.Uugs7RDBPWpzg9Yqgrse0f_iU-eYHj6YXPmpnAkjwH8"
}
```
For Secured API's follow the below instructions:
As secure API's  need token for processing the functionality of the API, copy the token when you recieve after logged in and paste it into Postman Authentication Header. You can watch video [Here](https://www.youtube.com/watch?v=LKveAwao9HA)

```
[POST METHOD]
3) /api/createstatus: (Secured API)
This API is for logged in user to upload status/post.
Request Data=>
{ "image_url":"URL-1", "caption":"This is a caption" }

Response=> If succeed you will receive response as follow otherwise error.
{
    "message": "Status is successfully uploaded",
    "id": "5ed4b517545ad540d4d57fe2"
}

[GET METHOD]
4) /api/status: (Secured API)
This API is for user to show their uploaded status.
Request Data: Just pass the token into header.

Response Data: All posts uploaded by the user logged in, user is identifying based on token.

{
    "_id": {
        "$oid": "5ed4b517545ad540d4d57fe2" This is status id 
    },
    "image_url": "URL-1",
    "caption": "Awesome",
    "comments": [ Comment if someone commented in this case here is one comment
        {
            "$oid": "5ed4b766fb5595f1252f8c3d" 
        }
    ],
    "likes": [], Likes if someone liked
    "added_by": { User id who created status
        "$oid": "5ed4b501545ad540d4d57fe1"
    },
    "time": "2020-06-01 13:28:15.332186"
}

[DELETE METHOD]
5) /api/deletestatus<statusid>: (secured API)
This method is user to delete the status created by the user.
Requset Data: Just pass the token into header.
Response Data:
{
    "message": "Your status is successfully deleted"
}

[GET METHOD]
5) /api/myinfo: (secured API)
This API for to get all information about a user. Based on token.
Request Data=> Nothing else other than passing token into Header.
Response=> If succeed you will get details like below otherwise appropriate error.
{
    "_id": {
        "$oid": "5ed4c6dfc28f5ef7483a8470"
    },
    "email": "shubhamjagdhane1010@gmail.com",
    "password": "$2b$12$c3gTGO.D34W9.LDP7mfNQ.ASUSgh0WWTmoPDODZNeovnFex..qbB2",
    "name": "Shubham Jagdhane",
    "status": [],
    "following": [],
    "followers": []
}

[POST METHOD]
6) /api/follow/<someother_user_id>: (secured API)
This API is to follow some other users.
Request Data=> Token in into the Header.
Response=> If succeed you will recieve as below otherwise error.
{
    "message": "You started following Shubham Jagdhane"
}

[POST METHOD]
7) /api/addcomment/<statusid>: (secured API)
This API is for to add comment for a status/posts, user can comment on its own posts/status or other users posts/status.
Request Data=> 
{
	"comment":"So great"
}

Response => 
{
    "message": "Your comment is succssfully added",
    "id": "5ed4b517545ad540d4d57fe2"
}

[DELETE METHOD]
8) /api/deletecomment/<commentid>: (secured API)
Request Data: Nothing
Response=> If succeed comment will be get deleted otherwise an appropriate error will display.

[POST METHOD]
9) /api/like/<statusid>: (secured API)
This API is to like a status/post added by user. User can like its own status/post or other user status/posts.
Request Data: Nothing in the body.
Response: 
{
    "message": "Your like this status",
    "id": "5ed4ca29c28f5ef7483a8472"
}

[DELETE METHOD]
10) /api/like/<like id>: (secured API)
Request Data: Nothing/Empty
Response: 
{
    "message": "You Dislike this status"
}


If you succeed for an API we will get expected result otherwise you will get an appropriate error.
```


## Built With Stack

* [Python](https://www.python.org/) - The language is used for implementation(python version 3.7.3)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [pipenv](https://pypi.org/project/pipenv/) - Dependency Management
* [MongoDB](https://www.mongodb.com/) - Database
* [MongoEngine](http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/) - MongoDB engine with flask
* [JWT](https://jwt.io/) - Used to generate token for user authentication
* [Unittest](https://docs.python.org/2/library/unittest.html) - The testing framework is used
* [MongoDB Compass](https://docs.mongodb.com/compass/master/install/) - The GUI for MongoDB

## Versioning
Version 1.1

