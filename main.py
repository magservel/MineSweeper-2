from flask import Flask, request, jsonify
import json
from minesManager import MinesManager
from minesChecker import MinesChecker
from bot import Bot

app = Flask(__name__)

manager = MinesManager()
checker = MinesChecker()
bot = Bot()
generatedJson = {}

@app.route('/')
def index():
    global manager
    manager = MinesManager()
    return app.send_static_file('index.html')

@app.route('/newGameData')
def newGameData():
    global generatedJson
    generatedJson = manager.getMines()
    return jsonify(generatedJson)

@app.route('/postMoveData', methods=['POST'])
def postMoveData():
    print "postMoveData"
    if not request.json:
        abort(400)
    res_json = bot.click_grid(request.json)
    ret = checker.checkMines(res_json)
    # ret_bot = bot.update_grid(ret)
    return jsonify(ret)
    
if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("8090"),
        debug=True
    )
