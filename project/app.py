from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from urllib.parse import quote_plus

app = Flask(__name__)

# Database configuration
DB_HOST = os.getenv("DB_HOST", "db_mysql")
DB_USER = os.getenv("DB_USER", "root")
#DB_PASSWORD = os.getenv("DB_PASSWORD", "root@123")
DB_PASSWORD = "root@123"

DB_NAME = os.getenv("DB_NAME", "flask_db")

print("---------")
DB_PASSWORD_ENCODED = quote_plus(DB_PASSWORD)
DB_PASSWORD_ENCODED = "root%40123"
print(DB_PASSWORD_ENCODED)

#app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD_ENCODED}@{DB_HOST}:3306/{DB_NAME}"
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD_ENCODED}@{DB_HOST}:3306/{DB_NAME}?ssl_disabled=true"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Assuming you have a table 'users' with columns 'id', 'name', 'email'
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))

# GET /users API
@app.route('/users', methods=['GET'])
def get_users():	 
    users = User.query.all()
    result = []
    for user in users:
        result.append({
            "id": user.id,
            "name": user.name,
            "email": user.email
        })
    return jsonify(result), 200
    
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pongupdatedv1"}), 200    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

