from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

class YourModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

@app.route('/add', methods=['POST'])
def add_entry():
    # Your logic to add an entry to the database
    pass

@app.route('/entries', methods=['GET'])
def get_entries():
    # Your logic to fetch entries from the database
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

