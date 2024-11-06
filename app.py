# PostgreSQL adapter for Python
import psycopg2
from flask import Flask
app = Flask(__name__)

# db connection string
db_conn = "postgresql://bball_render_practice_user:zDS09VBqss7InRDeoCxv1fHJpebyIhBf@dpg-cslsa3lumphs73bhvjr0-a/bball_render_practice")

@app.route('/db_test')
def testing():
	conn = psycopg2.connect(db_conn)
	conn.close()
	return "Successful Database Connection"

	
@app.route('/')
def hello_world():
    return 'Hello World from Matthew Presti in 3308'

@app.route('/db_create')
def create_tables():
	# Setup connection
	conn = psycopg2.connect(db_conn)
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
	
	# Save changes and cleanup
	con.commit()
	con.close()
	return "Basketball Table Created Successfully"

@app.route('/db_insert')
def insert_db():
	conn = psycopg2.connect(db_conn)
	cur = conn.cursor()
	cur.execute('''
	INSERT INTO Basketball (First, Last, City, Name, Number)
	Values
	('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
	('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
	('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
	('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
	''')
	con.commit()
	conn.close()
	
@app.route('/db_select')
def select_db():
	conn = psycopg2.connect(db_conn)
	cur = conn.cursor()
	
	# Get all players
	cur.execute('''
	SELECT * FROM Basketball;
	''')
	records = cur.fetchall()
	conn.close()
	
	# Build HTML table
	html_table = ''
	html_table += '<table>'
	
	# Add row for each player
	for player in records:
		html_table += '<tr>'
		for info in player:
			html_table += '<td>{}</td>'.format(info)
		html_table += '</tr>'
	html_table += '</table' 
	return html_table


@app.route('/db_drop')
def drop_db():
	conn = psycopg2.connect(db_conn)
	cur = conn.cursor()
	
	# Remove table
	cur.execute('''
	DROP TABLE Basketball;
	''')
	con.commit()
	conn.close()
	return "Basketball Table Dropped"
	
	
	
	
	
