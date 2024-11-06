import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/db_test')
def testing():
	conn = psycopg2.connect("postgresql://bball_render_practice_user:zDS09VBqss7InRDeoCxv1fHJpebyIhBf@dpg-cslsa3lumphs73bhvjr0-a/bball_render_practice")
	conn.close()
	return "Successful Database Connection"

	
@app.route('/')
def hello_world():
    return 'Hello World from Matthew Presti in 3308'

@app.route('/db_create')
def create_tables():
	conn = psycopg2.connect("postgresql://bball_render_practice_user:zDS09VBqss7InRDeoCxv1fHJpebyIhBf@dpg-cslsa3lumphs73bhvjr0-a/bball_render_practice")
	cur = conn.cursor()
	cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
		''')
	con.commit()
	con.close()
	
