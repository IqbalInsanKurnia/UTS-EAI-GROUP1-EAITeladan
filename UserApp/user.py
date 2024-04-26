from flask import Flask, jsonify
from flask_mysqldb import MySQL
from datetime import datetime
from werkzeug.utils import secure_filename
from flask import request

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'mysql-d48e9f6-bal-start.l.aivencloud.com'
app.config['MYSQL_PORT'] = 14160
app.config['MYSQL_USER'] = 'avnadmin'
app.config['MYSQL_PASSWORD'] = 'AVNS_HyawaTvSffYugyllPGf'
app.config['MYSQL_DB'] = 'user'
mysql = MySQL(app)

# Function to generate timestamp
def generate_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to get all user
@app.route('/user', methods=['GET'])
def get_all_user():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM user")
    columns = [i[0] for i in cursor.description]
    data = []
    for row in cursor.fetchall():
        data.append(dict(zip(columns, row)))
    cursor.close()
    timestamp = generate_timestamp()
    return jsonify({'timestamp': timestamp, 'data': data})

@app.route('/user/<paket_id>', methods=['GET'])
def get_user_by_paket_id(paket_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM user.user WHERE paket_id = %s", (paket_id,))
    columns = [i[0] for i in cursor.description]
    data = []
    for row in cursor.fetchall():
        data.append(dict(zip(columns, row)))
    cursor.close()
    timestamp = generate_timestamp()
    return jsonify({'timestamp': timestamp, 'data': data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)

