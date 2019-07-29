# API B2W 
###
## Tools used
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

## Example

### Requirements to use for test local

* [Python 3.6](https://www.python.org/)
* [Pip](https://pypi.org/project/pip/)
* [Pipenv](https://pipenv.readthedocs.io/en/latest/)
* [Mongo DB 4.0](https://www.mongodb.com/)
* [Postman](https://www.getpostman.com/)

1. enter in directory flask-b2w
2. run the command pip install pipenv
3. run the command pipenv install
4. run the command python application.py or make run

### Postman

1. Open postman.
2. Go to file tab and click import or Ctrl+O
3. Open file in directory flask-b2w/docs/API-B2W.postman_collection.json
4. Do the operations according to the documentation

### Using Postman for request client

#### List planets

![](https://github.com/viniciusnascimento95/flask-b2w/blob/master/docs/img/1_listplanet.png)

#### Create planet

![](https://github.com/viniciusnascimento95/flask-b2w/blob/master/docs/img/1_listplanet.png)

#### Put planet

![](https://github.com/viniciusnascimento95/flask-b2w/blob/master/docs/img/1_listplanet.png)

#### Delete planet

![](https://github.com/viniciusnascimento95/flask-b2w/blob/master/docs/img/1_listplanet.png)

#### Search by name

![](https://github.com/viniciusnascimento95/flask-b2w/blob/master/docs/img/1_listplanet.png) 

#### Entity this project

 - id
 - name 
 - climate
 - terrain
 - films
 - films_appearances
 - created_at

### Planets Actions

|Path|Method|Status Code|Description|
|:---|:----:|:---------:|:----------|
|`/planets`|`GET`|200|List all planets|
|`/planets/<string:planet_id>`|`GET`|200|Get a planet by id|
|`/planets`|`POST`|201|Create a planet|
|`/planets/<string:planet_id>`|`PUT`|200|Update all fields|
|`/planets/<string:planet_id>`|`DELETE`|204|Delete a planet|
|`/planets/name/<string:planet_name>`|`GET`|200|Get a planet by name|


### Run tests local

```shell
make test
```
