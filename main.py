from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route('/emails/create/')
def emails_create():
    name = request.args['name']
    emails = request.args['emails']
    con = sqlite3.connect('example.db')
    cur = con.cursor()
    sql = f"INSERT INTO emails (name, emails) VALUES ('{name}', '{emails}')"
    cur.execute(sql)
    con.commit()

    con.close()

    return 'KO1'


@app.route('/emails/read/')
def emails_read():
    id_ = request.args.get('id')

    con = sqlite3.connect('example.db')
    cur = con.cursor()

    # Create table
    if id_:
        sql = f'''SELECT * FROM emails WHERE id={id_};'''
    else:
        sql = f'''SELECT * FROM emails;'''
    cur.execute(sql)
    results = cur.fetchall()
    con.close()
    return str(results)


@app.route('/emails/update/')
def emails_update():
    id_ = request.args['id']
    name = request.args['name']

    import sqlite3
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    sql = f'''UPDATE emails SET name='{name}' WHERE id={id_};'''
    cur.execute(sql)
    con.commit()
    con.close()
    return 'KO'


@app.route('/emails/delete/')
def emails_delete():
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    sql = f'''DELETE FROM emails;'''
    cur.execute(sql)
    con.commit()
    con.close()
    return 'KO'


if __name__ == "__main__":
    app.run(debug=True)