from flask import Flask, render_template

app = Flask(__name__)

students = [
    {"id": 101, "name": "Arun", "course": "DevOps"},
    {"id": 102, "name": "Priya", "course": "Python"},
    {"id": 103, "name": "Rahul", "course": "AWS"}
]

@app.route('/')
def home():
    return render_template('index.html', students=students)

@app.route('/health')
def health():
    return {"status": "healthy"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
