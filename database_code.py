from app import app, db
from models import Task
from datetime import datetime

t = Task(title="xyz", date=datetime.utcnow())

with  app.app_context():
    db.create_all()
    db.session.add(t)
    db.session.commit()
    tasks = Task.query.all()

tasks

# external, to see queries
Task.query.all()