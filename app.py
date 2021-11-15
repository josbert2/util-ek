#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from forms import *
import os

#----------------------------------------------------------------------------#
# QR 
#----------------------------------------------------------------------------#
import pyqrcode
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#






app = Flask(__name__)
app.config.from_object('config')
#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
  
    return render_template('pages/placeholder.home.html')


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


@app.route('/login')
def login():
    form = LoginForm(request.form)
    return render_template('forms/login.html', form=form)


@app.route('/register')
def register():
    form = RegisterForm(request.form)
    return render_template('forms/register.html', form=form)


@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)

@app.route('/rrss')
def rrss():
   
    return render_template('pages/category-rrss.html')


@app.route('/history-random')
def historyRandom():
    when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
    who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
    name = ['Ali', 'Miriam','daniel', 'Hoouk', 'Starwalker']
    residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
    went = ['cinema', 'university','seminar', 'school', 'laundry']
    happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
    history = random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened)

    return render_template('pages/history-random.html', **locals())


@app.route('/qr-code', methods=['GET', 'POST'])
def qrCode():
    qrCode = request.form.get('qr-code-text')
    if qrCode is not None:
        if qrCode != '':
            print(1)
            link = qrCode
            qrGenerate = pyqrcode.create(link).svg('./static/img/qrcode.svg', scale=100)
            return render_template('pages/qr-code.html',  **locals())
            
        else:
            print(0)
            return render_template('pages/qr-code.html', **locals())
    else:
        qrCode = ''
        return render_template('pages/qr-code.html', **locals())
    
        



# Error handlers.


@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
