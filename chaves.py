# coding: utf-8

from flask import Flask, jsonify, render_template
from random import shuffle

app = Flask(__name__)
app.config.from_envvar('CHAVES_CONFIG', False)


@app.route('/videos/')
def videos():
    videos_list = app.config['VIDEOS']
    shuffle(videos_list)
    rv = []
    for video_seq in videos_list:
        rv.extend(video_seq)
    return jsonify(rv)


@app.route('/')
def home():
    return render_template('base.html')
