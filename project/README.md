curl http://127.0.0.1:5000/users

curl -X POST http://127.0.0.1:5000/users \
-H "Content-Type: application/json" \
-d '{"name":"Alice","email":"alice@gmail.com"}'


python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
python app.py

