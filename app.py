from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Def the Assistant model
class Assistant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    mobile = db.Column(db.String(20))
    email = db.Column(db.String(100))
    salary = db.Column(db.Float)
    city = db.Column(db.String(100))
    country = db.Column(db.String(100))
    department = db.Column(db.String(100))
    role = db.Column(db.String(100))

    def __repr__(self):
        return f'<Assistant {self.name}>'

# creating database tables
def create_db_tables():
    with app.app_context():
        db.create_all()

# Calling the function to create database tables
create_db_tables()

# Creating API endpoint
@app.route('/assistant', methods=['POST'])
def create_assistant():
    data = request.json
    assistant = Assistant(**data)
    db.session.add(assistant)
    db.session.commit()
    return jsonify({'message': 'Assistant created successfully'}), 201

# Reads all assistants API endpoint
@app.route('/assistants', methods=['GET'])
def get_assistants():
    assistants = Assistant.query.all()
    assistants_data = []
    for assistant in assistants:
        assistant_data = {
            'id': assistant.id,
            'name': assistant.name,
            'mobile': assistant.mobile,
            'email': assistant.email,
            'salary': assistant.salary,
            'city': assistant.city,
            'country': assistant.country,
            'department': assistant.department,
            'role': assistant.role
        }
        assistants_data.append(assistant_data)
    return jsonify(assistants_data)

# Reading single assistant API endpoint
@app.route('/assistant/<int:assistant_id>', methods=['GET'])
def get_assistant(assistant_id):
    assistant = Assistant.query.get_or_404(assistant_id)
    return jsonify({
        'id': assistant.id,
        'name': assistant.name,
        'mobile': assistant.mobile,
        'email': assistant.email,
        'salary': assistant.salary,
        'city': assistant.city,
        'country': assistant.country,
        'department': assistant.department,
        'role': assistant.role
    })

# Updating API endpoint
@app.route('/assistant/<int:assistant_id>', methods=['PUT'])
def update_assistant(assistant_id):
    assistant = Assistant.query.get_or_404(assistant_id)
    data = request.json
    for key, value in data.items():
        setattr(assistant, key, value)
    db.session.commit()
    return jsonify({'message': 'Assistant updated successfully'}), 200

# Deleting API endpoint
@app.route('/assistant/<int:assistant_id>', methods=['DELETE'])
def delete_assistant(assistant_id):
    assistant = Assistant.query.get_or_404(assistant_id)
    db.session.delete(assistant)
    db.session.commit()
    return jsonify({'message': 'Assistant deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
