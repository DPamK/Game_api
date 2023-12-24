from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
users = {
    "admin":"password"
}

@auth.verify_password
def verify_password(username,password):
    if username in users and users[username] == password:
        return username
@auth.error_handler
def unauthorized():
    return {
        'error':'Unauthorized access'
    },401
    

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)
api = Api(app)
ma = Marshmallow(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120))

class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


with app.app_context():
    db.create_all()

class TaskResource(Resource):
    def get(self):
        tasks = Task.query.all()
        return tasks_schema.dump(tasks)
    
    def post(self):
        task_data = task_schema.load(request.json)
        task = Task(**task_data)
        db.session.add(task)
        db.session.commit()
        return  task_schema.dump(task), 201
    
api.add_resource(TaskResource,'/tasks')

@app.errorhandler(400)
def bad_request(e):
    return {'error': 'Bad request'}, 400 

@app.route('/secure-endpoint')
@auth.login_required
def secure_endpoint():
    return {'message': f"Hello, {auth.current_user()}"}

if __name__=="__main__":
    app.run(debug=True)