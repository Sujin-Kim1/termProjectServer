import sqlite3
import json

from flask import Flask, flash, redirect, render_template, \
     request, url_for, jsonify
from app import app

# https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en

### URL Handling
HTML = '''
  <!doctype html>
  <title>API Server</title>
  <h1>API Server</h1>
  <p> This is API server for 'Mobile Programming' </p>
'''

@app.route('/')
@app.route('/index')
def index():
    return HTML


@app.route('/api/pick')
def pick():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    rows = c.execute("SELECT * FROM pick")
    data = []
    for r in rows:
        d = {}
        d['title'] = r[0]
        d['name'] = r[1]
        d['info'] = r[2]
        d['url'] = r[3]
        d['address'] = r[4]
        d['time'] = r[5]
        data.append(d)
    print(json.dumps(data))
    return jsonify(data)


@app.route('/api/pick/<name>')
def pick_name(name):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    rows = c.execute("SELECT * FROM pick WHERE name = '%s' " % name)
    data = [r for r in rows]
    print(data)

    return jsonify(data)


@app.route('/api/pick', methods=['POST'])
def pick_post():
    print(request.form)
    for k, v in request.form.items():
        print(k, v)
    d = request.form
    sql = "INSERT INTO pick VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % \
           (d['title'], d['name'], d['info'], d['url'], d['address'], d['time'])
    try:
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        res = c.execute(sql)
        conn.commit()
        print(res)
        res = True
    except:
        res = False
        pass
    return jsonify(res)


@app.route('/api/pick', methods=['PUT'])
def pick_put():
    d = request.form
    sql = "UPDATE pick SET info = '%s', url = '%s', address = '%s', time = '%s' WHERE title = '%s', name = %s " % \
           (d['info'], d['url'], d['address'], d['time'], d['title'], d['name'])

    try:
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        res = c.execute(sql)
        conn.commit()
        print(res)
        res = True
    except:
        res = False
        raise
        pass
    return jsonify(res)


@app.route('/api/pick/name/<name>', methods=['DELETE'])
def pick_delete(name):
    sql = "DELETE FROM pick WHERE name = '%s' " % (name)
    try:
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        res = c.execute(sql)
        conn.commit()
        print(res)
        res = True
    except:
        res = False
        pass
    return jsonify(res)


@app.route('/api/nearby/')
def brand():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    rows = c.execute("SELECT * FROM nearby")

    data = []
    for r in rows:
        d = {}
        d['name'] = r[0]
        d['lat'] = r[1]
        d['lng'] = r[2]
        data.append(d)
    print(json.dumps(data))
    return jsonify(data)

@app.route('/api/nearby/<name>')
def brand_name(name):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    rows = c.execute("SELECT * FROM nearby WHERE name = '%s' " % name)
    data = [r for r in rows]
    print(data)

    return jsonify(data)

@app.route('/api/nearby/<name>', methods=['DELETE'])
def brand_delete(name):
    sql = "DELETE FROM nearby WHERE name = '%s' " % (name)
    try:
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        res = c.execute(sql)
        conn.commit()
        print(res)
        res = True
    except:
        res = False
        pass
    return jsonify(res)

