from app import app
from flask import render_template, url_for, request, session, jsonify, redirect
import lyricsgenius as genius
import pickle
import sklearn

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/searchGenius', methods=['GET', 'POST'])
def searchGenius():
    if request.method == "POST":
        return redirect(url_for('search', song_name=request.form['searchBar']))
    return 'Bad Request'
    
@app.route('/search/<song_name>', methods=['GET'])
def search(song_name):
    genres = ['Rap', 'Rock', 'Country']
    if song_name:
        api = genius.Genius('4vPfh0l1I33h0qqY-Bzn1ITfTGl_MPnKBHRRk_8XgvKnX70r9bumFYPWRkJ2VNSl')
        lyric = api.search_song(song_name).lyrics
        model = pickle.load(open('app/random_forest.pkl', 'rb'))
        result = model.predict([lyric])
        return render_template('results.html', genre=genres[result[0]], song_name=song_name)
    else:
        return render_template('results.html')
        
@app.route('/search/')
def blanksearch():
    return render_template('results.html')
        