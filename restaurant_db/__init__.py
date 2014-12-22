from flask import Flask
app = Flask(__name__)

app.secret_key="gabe and kevin"

import restaurant_db.routes
from restaurant_db.rdb import db

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://rdb:rdb@localhost/Food'

db.init_app(app)


