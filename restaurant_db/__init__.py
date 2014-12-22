from flask import Flask
app = Flask(__name__)

app.secret_key="gabe and kevin"

import restaurant_db.routes

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://rdb:rdb@localhost/Food'

