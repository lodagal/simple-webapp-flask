FROM python
COPY . /opt/app-code
Run pip install flask
Run pip install flask-mysql
ENTRYPOINT FLASK_APP=/opt/app-code/app.py flask run --host=0.0.0.0 
