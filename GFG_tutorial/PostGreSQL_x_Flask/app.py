from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database='flask_db', user='postgres',
                        password='1234', host='localhost', port='5432')

cur = conn.cursor()

cur.execute(
    '''create table if not exists products (id serial \
        primary key, name varchar(100), price float);''')

cur.execute(
    '''insert into products (name, price) values \
        ('Apple', 1.99), ('Orange', 0.99), ('Banana', 0.59);''')

conn.commit()

cur.close()
conn.close()

@app.route('/')
def index():
    conn = psycopg2.connect(database='flask_db',
                            user='postgres',
                            password='1234',
                            host='localhost', port='5432')
    
    cur = conn.cursor()
    
    cur.execute('''SELECT * FROM products''')  # ← Fix here

    data = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('index.html', data=data)

@app.route('/create', methods=['POST'])
def create():
    conn = psycopg2.connect(database='flask_db',
                            user='postgres',
                            password='1234',
                            host='localhost', port='5432')
    
    cur = conn.cursor()

    name = request.form['name']
    price = request.form['price']

    cur.execute(
        '''insert into products \
            (name, price) values (%s, %s)''',
            (name, price))
    
    conn.commit()

    cur.close()
    conn.close()

    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update():
    conn = psycopg2.connect(database='flask_db',
                            user='postgres',
                            password='1234',
                            host='localhost', port='5432')
    
    cur = conn.cursor()

    name = request.form['name']
    price = request.form['price']
    id = request.form['id']

    cur.execute(
        '''update products set name=%s, \
            price=%s where id=%s''', (name, price, id))
    
    conn.commit()
    return redirect(url_for('index'))

@app.route('/delete', methods=['post'])
def delete():
    conn = psycopg2.connect(database='flask_db', user='postgres',
     password='1234',
     host='localhost', port='5432')
    cur = conn.cursor()

    id = request.form['id']
    cur.execute('''delete from products where id=%s''', (id,))

    conn.commit()

    cur.close()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)