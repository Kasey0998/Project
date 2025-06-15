from flask import Flask 
from flaskext.mysql import MySQL


app = Flask(__name__)
mysql=MySQL(app)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_DB'] = 'CRM' 
app.config['MYSQL_DATABASE_PORT'] = 8889

mysql.init_app(app)

conn = mysql.connect()
if conn:
    print("Connected to the database successfully")
else:
    print("Failed to connect to the database")




@app.route('/user')

def get_users():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user")
    users = cursor.fetchall()
    cursor.close()
    print(users)
    return {'users': users}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
