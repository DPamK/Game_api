from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_security import Security, SQLAlchemySessionUserDatastore, login_required
from flask_security.utils import hash_password
from user_security import User, Role
from models import Task
from app_config import app, db


# 身份验证
user_datastore = SQLAlchemySessionUserDatastore(db,User,Role)
security = Security(app,user_datastore)

# restful_api
api = Api(app)

# 对象序列化/反序列化库，验证和格式化API响应
ma = Marshmallow(app)
class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


with app.app_context():
    db.create_all()

class TaskResource(Resource):
    @login_required
    def get(self):
        tasks = Task.query.all()
        return tasks_schema.dump(tasks)
    
    @login_required
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

if __name__=="__main__":
    app.run(debug=True)
