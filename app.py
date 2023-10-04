from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def users() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'docker_test'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users')
    results = [{email: password} for (email, password) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return json.dumps({'user': users()})


if __name__ == '__main__':
    app.run(debug=True)