from flask import Flask, jsonify, abort, request
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome!"


@app.route('/getInfo', methods=['GET'])
def topFive():
    cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='whois')
    with cnx.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute('SELECT * FROM whois')
        data = cursor.fetchall()
            
    cnx.close()
    return jsonify({'data' : data})

if __name__ == '__main__':
    app.run(debug=True)