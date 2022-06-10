from flask import Flask, jsonify , request
from flask_cors import CORS
import sys


# Rememeber to LOCK DOWN api after testing, Leaving CORS OPEN IS dangerous
app = Flask(__name__)
CORS(app)

tweets = [
    "Sick of having to go to 2 different buts to buy pizza and sungalasses",
    "This is the most annoying part of the assignment",
    "I hate applying concepts from my English high school experience",
    "I hope I'm doing this first step correctly",
    "Hello World",
    "You know , I'm sure I could've just used shorter quotes",
    "True"
]

@app.get('/api/Tweets')
def tweets_get():
    args = request.args
    # tweetId
    tweet_Id = int(args.get('tweetId'))
    # if not tweet_id (alternative)
    if tweet_Id == None:
        return jsonify(tweets) , 200
    else:
        return jsonify(tweets[tweet_Id]), 200
    


# Always goes last 
if len(sys.argv) > 1 :
    mode =sys.argv[1]
else :
    print("Missing required argument: testing | production")
    exit()
if mode == "testing":
    # Only want CORS on testing servers not production servers
    CORS(app)
    print("Runnng in testing mode !")
    app.run(debug=True)
elif mode == "production" :
        import bjoern
        print("Running in production mode!")
        bjoern.run(app, "0.0.0.0" , 5000)
else:
    print("Invalid mode , must be one of :testing | production")
    exit()
        

# Always goes last 
