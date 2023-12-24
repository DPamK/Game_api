import unittest
from api import app,db,Task
from flask_testing import TestCase

class AppTestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
        return app
    
    def setUP(self):
        db.create_all()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
    def test_task_creation(self):
        task = Task(title='Test Task')
        db.session.add(task)
        db.session.commit()

        tasks_in_db = Task.query.all()
        self.assertEqual(len(tasks_in_db),1)
        self.assertEqual(tasks_in_db[0].title, "Test Task")