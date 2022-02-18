from flask import Flask, request
import time
import random
import string

app = Flask(__name__)


@app.route('/whoami/')
def whoami():
    browser = request.user_agent.browser
    ip = request.remote_addr
    time_server = time.strftime('%A %B, %d %Y %H:%M:%S')
    return f'Browser : {browser}, Ip : {ip}, Time_Server : {time_server}'


@app.route('/source_code/')
def source_code():
    with open('flask application.py', 'r') as file:
        source_code_my = file.read()
    return source_code_my


@app.route('/random/')
def random_abc():
    length = request.values.get('length', '')
    specials = request.values.get('specials', '0')
    digits = request.values.get('digits', '0')
    alfa = ''
    if int(length) in range(1, 101):
        if int(specials) == 0 and int(digits) == 0:
            alfa = string.ascii_letters
        if int(specials) == 1 and int(digits) == 0:
            alfa = string.ascii_letters + '!"№;%:?*()_+.'
        if int(specials) == 1 and int(digits) == 1:
            alfa = string.ascii_letters + '!"№;%:?*()_+.' + '0123456789'
        if int(specials) == 0 and int(digits) == 1:
            alfa = string.ascii_letters + '0123456789'
    if alfa:
        random_choice = random.choices(alfa, k=int(length))
    else:
        random_choice = None
    return f'Random Length : {random_choice}'


app.run(debug=True)
