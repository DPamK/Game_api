from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.sqlite3'
db = SQLAlchemy(app)
api = Api(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120))

db.create_all()

class TaskResource(Resource):
    def get(self):
        tasks = Task.query.all()
        return [{'id': task.id, 'title': task.title, 'description': task.description} for task in tasks]
    
    def post(self):
        task_data = request.json
        task = Task(title=task_data['title'], description=task_data.get('description'))
        db.session.add(task)
        db.session.commit()
        return  {'id': task.id, 'title': task.title, 'description': task.description}, 201
    
api.add_resource(TaskResource,'/tasks')

if __name__=="__main__":
    app.run(debug=True)