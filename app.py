from flask import Flask, render_template, request
from flask_wtf import Form
from wtforms import StringField, SubmitField
# from wtforms.validator import Required, Length

import random

app = Flask(__name__)

# global variables
numberOfEmojies = 5
emotionIdentifier = None

# Home Page
# Get the values from emotion slider
@app.route('/', methods=['GET', 'POST'])
def index():
    global emotionIdentifier
    if request.method == 'POST' and 'name' in request.form:
        value = request.form['name']
    else:
        value = 50
    emotionIdentifier = value
    emotion = emotionFinder(int(value))
    emojies = throwEmoji(emotion)
    return render_template('index.html', value = value, emojies = (random.choice(emojies)*numberOfEmojies))  


# Display Emojies
@app.route('/<value>', methods=['GET', 'POST'])
def index_withEmojies(value):
    global emotionIdentifier
    if request.method == 'POST' and 'name' in request.form:
        value = request.form['name']
    emotion = emotionFinder(int(value))
    emotionIdentifier = value
    emojies = throwEmoji(emotion)
    return render_template('index.html', emojies = (random.choice(emojies)*numberOfEmojies))


# User Login Page
@app.route('/user/login/<userName>')
def login(userName):
    return render_template('userLogin.html', name = userName)


# error pages handler
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


# change default
def changeDefault(number):
    global numberOfEmojies
    numberOfEmojies = number


# Discover Emotion
def emotionFinder(value):
    if(value >= 90):
        return 'veryHappy'
    elif(value >= 70 and value < 90):
        return 'happy'
    elif(value >= 30 and value < 70):
        return 'nothing'
    elif(value >= 10 and value < 30):
        return 'sad'
    elif(value >= 0 and value <10):
        return 'verySad'


# get emotion and return emojis
def throwEmoji(emotion):
    from emojiHouse import emojiHouse
    home = emojiHouse(emotion)
    throw = home.port()
    return (throw)


if __name__ == '__main__':
    app.run(debug= True)