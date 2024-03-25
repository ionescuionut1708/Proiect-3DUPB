import pymongo
import certifi
import gridfs

uri = "mongodb+srv://ionescuionut1708:K2eLsZLTBkb3HeCp@cluster0.gf5oaax.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri, tlsCAFile=certifi.where())
database = client["web_dev"]
fs = gridfs.GridFS(database)

userCollection = database["users"]
userList = [
    {"username": "spiderman99", "email": "ionescuionut1708@gmail.com", "password": "panda1234"},
    {"username": "princessLEIA", "email": "ionescuionut1708@gmail.com", "password": "panda1234"},
    {"username": "gereltOfRivia", "email": "ionescuionut1708@gmail.com", "password": "panda1234"},
    {"username": "ezio_auditore", "email": "ionescuionut1708@gmail.com", "password": "panda1234"},
    {"username": "nathan_drake99", "email": "ionescuionut1708@gmail.com", "password": "panda1234"}
]



userIDs = userCollection.insert_many(userList) #intoarce un ID unic pt fiecare user
# print(userIDs.inserted_ids)
# print("\nAici este primul ID: {}".format(userIDs.inserted_ids[0]))
print("\n")

# for index, value in enumerate(userIDs.inserted_ids):
#     userList[index]["username"] = value


gamesCollesction = database["games"]
gameList = [
    {"title": "Balloons Madness", "description": "Try beat your friends' high scores by shooting as many balloons as possible before the time runs out!", "image": ""},
    {"title": "Endless Runner", "description": "How long can you survive in this amazing endless runner? Can you beat the hight scores of other players? Try it now!", "image": ""}
]

try:
    file1 = open("balloons.jpg", "rb")
    content1 = file1.read()
    out1 = fs.put(content1, filename = "balloons.jpg")
    gameList[0]["image"] = out1

    try:
        file2 = open("runner.jpg", "rb")
        content2 = file2.read()
        out2 = fs.put(content2, filename = "runner.jpg")
        gameList[1]["image"] = out2

        gameIDs = gamesCollesction.insert_many(gameList)

        # for index, value in enumerate(gameIDs.inserted_ids):
        #     gameList[index]["title"] = value

        highScoresCollection = database["scores"]
        highScoresList = [
            {"game": "Balloons Madness", "user": "spiderman99", "score": 67},
            {"game": "Endless Runner", "user": "spiderman99", "score": 55},
            {"game": "Endless Runner", "user": "princessLEIA", "score": 109},
            {"game": "Balloons Madness", "user": "gereltOfRivia", "score": 73},
            {"game": "Balloons Madness", "user": "ezio_auditore", "score": 45},
            {"game": "Endless Runner", "user": "nathan_drake99", "score": 77}
        ]
       
        # for element in highScoresList:
        #     index = 0
        #     for element_userList in userList:
        #         if(element["user"] == element_userList["username"]):
        #             element["user"] = userIDs.inserted_ids[index]                
        #         index = index + 1
        #     index_2 = 0
        #     for element_gameList in gameList:
        #         if(element["game"] == element_gameList["title"]):
        #             element["game"] = gameIDs.inserted_ids[index_2]
        #         index_2 = index_2 + 1

        highScoresIDs = highScoresCollection.insert_many(highScoresList)
    except:
        print("Error uploading runner photo!")
except:
    print("Error uploading balloons photo!")

# try:
#     file = open("balloons.jpg", "rb")
#     content = file.read()
#     out = fs.put(content, filename = "balloons.jpg") #primesc ca rezultat un ID (am incarcat imaginea)
#     print(out)
#     try:
#         out2 = fs.get(out)
#         file2 = open("balloons2.jpg", "wb")
#         byteArray = out2.read()
#         file2.write(byteArray)
#     except:
#         print("Error downloading the photo!")
# except:
#     print("Error uploading photo!")
