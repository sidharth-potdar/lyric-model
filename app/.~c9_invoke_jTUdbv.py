from app import app
from flask import render_template, url_for, request, session, jsonify
# import lyricsgenius as genius

@app.route('/')
def index():
    return render_template('index.html')
    
#accepts input as JSON, in form:
# {
#    "song_name": datafromsearchbarasstring
# }
# returns JSON:
# {
#    "genre": resultgenre,
#    "accuracy": resultaccuracy
# }
@app.route('/searchGenius', methods=['GET', 'POST'])
def searchGenius():
    if request.method == "POST":
        print(request.data['song'])
        title = rjson['song_name']
        api = genius.Genius('4vPfh0l1I33h0qqY-Bzn1ITfTGl_MPnKBHRRk_8XgvKnX70r9bumFYPWRkJ2VNSl')
        testinput = {"song_name": "God's Plan"}
        lyric = api.search_song(title).lyrics
        return request.get_json()
    return request