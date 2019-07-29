FROM python:3.6-alpine

RUN mkdir /code

ADD Pipfile Pipfile.lock /code/

RUN python3 -m pip install pipenv

WORKDIR /code

RUN pipenv install 

CMD [ "python" , "application.py" ]