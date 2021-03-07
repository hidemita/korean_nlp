# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import json

from konlpy.tag import Okt
okt = Okt()

app = Flask(__name__)


@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/echo', methods=['GET', 'POST'])
def echo():
    if request.method == 'POST':
        if 'q' in request.form:
            query = request.form['q']
        elif 'query' in request.form:
            query = request.form['query']
        else:
            query = ''
    else:
        query = request.args.get('q')
        if not query:
            query = request.args.get('query')
        if not query:
            query = ''

    return query

@app.route('/test', methods=['GET', 'POST'])
def test():
    sentence = '' # if no valid query, return results for empty.
    norm = False
    stem = False

    content = request.json
    if content:
        if 'sentence' in content:
            sentence = content['sentence']
        if 'stem' in content:
            stem = content['stem']
        if 'norm' in content:
            norm = content['norm']

    parse_result = okt.pos(sentence, norm=norm, stem=stem)
    r = []
    for e in parse_result:
        print(e)
        r.append(list(e))

    return jsonify({
        "sentence" : f"{sentence}",
        "norm" : norm,
        "stem" : stem,
        "result" : r
    })

# server program entry point
app.run(host='0.0.0.0', port=8080, debug=True)
