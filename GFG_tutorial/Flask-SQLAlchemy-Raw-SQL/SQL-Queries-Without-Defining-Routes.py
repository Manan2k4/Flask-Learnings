from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text  # Import 'text' for executing raw SQL

# CREATE THE FLASK APP
app = Flask(__name__)

# DATABASE CONFIGURATION
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Manan2k4%40MySQL@127.0.0.1:3306/demo"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# INITIALIZE DATABASE
db = SQLAlchemy(app)

# EXECUTE RAW SQL QUERIES WITH PROPER CONNECTION
with app.app_context():
    with db.engine.connect() as connection:
        # CREATE TABLE IF NOT EXISTS
        connection.execute(text('''
            CREATE TABLE IF NOT EXISTS users (
                email VARCHAR(50),
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                passwd VARCHAR(50)
            );
        '''))
        
        # INSERT DATA INTO users TABLE
        connection.execute(text('''
            INSERT INTO users(email, first_name, last_name, passwd) VALUES 
            ('john.doe@zmail.com', 'John', 'Doe', 'john@123'),
            ('john.doe@zmail.com', 'John', 'Doe', 'johndoe@777'),
            ('noah.emma@wmail.com', 'Emma', 'Noah', 'emaaa!00'),
            ('emma@tmail.com', 'Emma', 'Noah', 'whrfc2bfh904'),
            ('noah.emma@wmail.com', 'Emma', 'Noah', 'emaaa!00'),
            ('liam.olivia@wmail.com', 'Liam', 'Olivia', 'lolivia#900'),
            ('liam.olivia@wmail.com', 'Liam', 'Olivia', 'lolivia$345');
        '''))
        
        # COMMIT CHANGES
        connection.commit()
        
        # FETCH RECORDS FROM users TABLE
        result = connection.execute(text('SELECT * FROM users;'))
        for record in result:
            print(record)

# RUN THE APP
if __name__ == '__main__':
    app.run()