# API B2W 
### Tools used
* __python-dotenv__
* __flask__
* __Flask restfull__
* __Mongodb__
* __MongoEngine__ 
*  __Pymongo__
* __Flask-Marshmallow__
* __ipython__ 
* __ipdb__ 
* __flask-shell-ipython__ 
* __isort__ 
* __pytest-flask__ 
* __flake8__ 
* __pytest__ 
* __pytest-cov__ 
* __pytest-runner__ 
* __Faker__ 
* __flask-mongoengine__ 
* __gunicorn__ 
* __marshmallow__ 

### Project description

Flask-B2W is a Restful API, a CRUD of planets was implemented using MongoDB database, this challenge for the backend developer position on B2W DIGITAL.

### Requirements to use

* [Python 3.6](https://www.python.org/)
* [Pip](https://pypi.org/project/pip/)
* [Pipenv](https://pipenv.readthedocs.io/en/latest/)
* [Mongo DB 4.0](https://www.mongodb.com/)
* [Postman](https://www.getpostman.com/)

1. enter in directory flask-b2w
2. run the command pip install pipenv
3. run the command pipenv install
4. run the command python application.py
5. use Postman for request client

### Postman

1. Open postman.
2. Go to file tab and click import or Ctrl+O
3. Open file in directory flask-b2w/docs/API-B2W.postman_collection.json
4. Do the operations according to the documentation

#### Model using for this project

 - name 
 - climate
 - terrain

### Planets Actions

|Path|Method|Status Code|Description|
|:---|:----:|:---------:|:----------|
|`/api/planets/`|`OPTIONS`|200|Shows Planets Resource structure|
|`/api/planets/`|`GET`|200|List all planets|
|`/api/planets/:id`|`GET`|200|Get a planet object|
|`/api/planets/`|`POST`|201|Create a planet|
|`/api/planets/:id`|`PUT`|200|Update all fields on a planet object|
|`/api/planets/:id`|`DELETE`|204|Delete a planet|
