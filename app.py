from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import time 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:nitin123@db:5432/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)



@app.route('/')
def home():
    return "Hello"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    all_tasks = []
    for task in tasks:
        all_tasks.append({
            'id' : task.id,
            'title' : task.title,
            'description' : task.description
        })
    return jsonify(all_tasks)


@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = Task(
        title=data['title'],
        description=data['description']
        )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({
        'message': 'Task added successfully',
        'task': {
            'id': new_task.id,
            'title': new_task.title,
            'description': new_task.description
        }
    }), 201

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({
            "message": "Task deleted successfully"
        })
    else:
        return jsonify({
            "message": "Task not found"
        }), 404
    
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)
    if task:
        data = request.get_json()
        task.title = data['title']
        task.description = data['description']
        db.session.commit()
        return jsonify({
            "message": "Task updated successfully",
            "task": {
                "id": task.id,
                "title": task.title,
                "description": task.description
            }
        })
    else:
        return jsonify({
            "message" : "Task not found"
        }), 404
    

@app.route('/tasks/<int:id>', methods=['PATCH'])
def up_date_task(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({
            "message" : "Task not found"
        }), 404
    data = request.get_json()
    if "title" in data:
        task.title = data['title']
    
    if "description" in data:
       task.description = data['description']

    db.session.commit()

    return jsonify({
        "message": "Task updated successfully",
        "task": {
            "id": task.id,
            "title": task.title,
            "description": task.description
        }
    })

if __name__ == '__main__':
    time.sleep(10)
    
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=8000, debug=True)