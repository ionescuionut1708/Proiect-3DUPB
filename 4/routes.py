from flask import Flask, abort, jsonify, request
from flask_cors import cross_origin
from bson.objectid import ObjectId
from flask_cors import CORS

import pymongo
import certifi
import gridfs

uri = "mongodb+srv://ionescuionut1708:K2eLsZLTBkb3HeCp@cluster0.gf5oaax.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri, tlsCAFile=certifi.where())
database = client["web_dev"]
fs = gridfs.GridFS(database)

userCollection = database["users"]
gameCollection = database["games"]
scoreCollection = database["scores"]

app = Flask(__name__)
CORS(app)

@app.errorhandler(Exception)
def handle_error(e):
    return jsonify(error=str(e)), 500

@app.route('/getGames', methods = ['GET'])
@cross_origin(supports_credentials = True)
def get_games():
    result = [] 
    for score in gameCollection.find():
        result.append({'_id': str(score['_id']), 'title': score['title'], 'description': score['description'], 'image': str(score['image'])}) 
    return jsonify(result = result)

@app.route('/getImageById/<id>', methods = ['GET'])
@cross_origin(supports_credentials = True)
def get_image(id):
    out = fs.get(ObjectId(id))
    return out.read()

@app.route('/getScores', methods = ['GET'])
@cross_origin(supports_credentials = True)
def get_scores():
    result = [] 
    for score in scoreCollection.find():
        result.append({'_id': str(score['_id']), 'game': str(score['game']), 'user': str(score['user']), 'score': score['score']}) 
    return jsonify(result = result) #variabila in care am salvat rezultatul

@app.route('/getScoresByGameName/<game>', methods = ['GET']) #am pus valoarea variabilei game intre <>
@cross_origin(supports_credentials = True)
def get_scores_game_name(game):
    #obj_game_id = ObjectId(game) #stringul numele game-ului trebuie transformat din nou un ObjId pentru a fi gasit in aza de date
    result = []
    query = {'game': game}  #query = {'game': obj_game_id}
    document = scoreCollection.find(query)

    for score in document:
        result.append({'_id': str(score['_id']), 'game': str(score['game']), 'user': str(score['user']), 'score': score['score']}) 
    return jsonify(result = result)

@app.route('/getScoreById/<id>', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_score(id):
    query = {'_id': ObjectId(id)}
    document = scoreCollection.find_one(query)
    if not document:
        abort(404, description="Score not found with given ID")
    return jsonify(result=document['score'])

@app.route('/addScore', methods=['POST', 'PUT'])
@cross_origin(supports_credentials=True)
def add_scores():
    data = request.json
    requested_id = None

    # Validați dacă toate cheile necesare există
    if not all(key in data for key in ('game', 'user', 'score')):
        abort(400, description="Missing required data")

    data['score'] = int(data['score'])

    if request.method == 'POST':
        requested_id = scoreCollection.insert_one(data).inserted_id
    elif request.method == 'PUT':
        result = scoreCollection.update_one(
          {'game': data['game'], 'user': data['user']}, 
          {'$set': {'score': data['score']}}, 
          upsert=True
        )
        requested_id = result.upserted_id if result.upserted_id else data['_id']
    else:
        abort(405, description="Method not allowed")

    return jsonify(id=str(requested_id))


@app.route('/login', methods=['POST'])
@cross_origin(supports_credentials = True)
def login():
    result = request.json 
    username = result.get('username')
    password = result.get('password')
    
    user = userCollection.find_one({'username': username, 'password': password})
    
    if user:
        return jsonify(message='Login successful'), 200
    else:
        return jsonify(message='Invalid credentials'), 401


@app.route('/register', methods=['POST'])
@cross_origin(supports_credentials=True)
def register():
    data = request.json
    
    required_fields = ('username', 'password', 'email')
    if not all(key in data for key in required_fields):
        abort(400, description="Username, email, and password are required")

    existing_user_by_username = userCollection.find_one({'username': data['username']})
    existing_user_by_email = userCollection.find_one({'email': data['email']})

    if existing_user_by_username:
        return jsonify(message='Username already exists'), 400
    if existing_user_by_email:
        return jsonify(message='Email already exists'), 400

    user_data = {
        'username': data['username'],
        'email': data['email'], 
        'password': data['password'],
    }
    userCollection.insert_one(user_data)

    return jsonify(message='User registered successfully'), 201



if __name__ == "__main__":
    app.run()


