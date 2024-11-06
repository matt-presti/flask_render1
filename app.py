import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route(/'db_test')
def testing():
	conn = psycopg2.connect("postgresql://bball_render_practice_user:zDS09VBqss7InRDeoCxv1fHJpebyIhBf@dpg-cslsa3lumphs73bhvjr0-a/bball_render_practice")
	conn.close()
	return "Successful Database Connection"

	
@app.route('/')
def hello_world():
    return 'Hello World from Matthew Presti in 3308'
