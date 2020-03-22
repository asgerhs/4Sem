from flask import Flask, jsonify, abort, request
import pymysql

app = Flask(__name__)

people = [
    {
        'id' : 1,
        'first_name' : u'Artem',
        'last_name' : u'Ivanov',
        'age' : 22
    },
    {
        'id' : 2,
        'first_name' : u'Astrid',
        'last_name' : u'Cordes',
        'age' : 22
    },
    {
        'id' : 3,
        'first_name' : u'Alex',
        'last_name' : u'Valentin',
        'age' : 23
    },
    {
        'id' : 4,
        'first_name' : u'William',
        'last_name' : u'Huusfeldt',
        'age' : 30
    }
]

@app.route('/')
def index():
    return "Hello, World from flask server!"

@app.route('/datagenerator/api/person/<int:ammount>', methods=['GET'])
def get_people(ammount):

    cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='test')
    with cnx.cursor() as cursor:
        cursor.execute('SELECT * FROM person LIMIT {ammount}'.format(ammount=ammount))
        data = cursor.fetchall()
    cnx.close()
    return jsonify({'persons': data})





@app.route('/datagenerator/api/person', methods=['POST'])
def create_person():
    cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='test')
    with cnx.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute('SELECT * FROM person')
        data = cursor.fetchall()
    
        person = {
            'personId': data[-1]['personId'] + 1,
            'firstName': request.json['firstName'],
            'lastName': request.json['lastName']
        }
        cursor.execute('INSERT INTO person VALUES (%(personId)s, %(firstName)s, %(lastName)s)', (person))
        cnx.commit()
    cnx.close()
    return jsonify({'person' : person}), 201


if __name__ == '__main__':
    app.run(debug=True)