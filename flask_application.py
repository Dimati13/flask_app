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
    return f'''
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    <title>Whoami</title>
  </head>
  <body>

    <!-- Option 2: Separate Popper and Bootstrap JS -->

    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>

    <dl class="row">
      <dt class="col-sm-3">Browser</dt>
      <dd class="col-sm-9">{browser}</dd>

      <dt class="col-sm-3">IP</dt>
      <dd class="col-sm-9">{ip}</dd>

      <dt class="col-sm-3">Time Server</dt>
      <dd class="col-sm-9">{time_server}</dd>

    </dl>
  </body>
  <a href="/"> Home </a>
</html>
'''


@app.route('/source_code/')
def source_code():
    with open('flask_application.py', 'r') as file:
        source_code_my = file.read()
    return f'''
<form>
    <pre>
        {source_code_my} <br/>
        <a href="/"> Home </a>
    </pre>
</form>
'''


@app.route('/random/')
def random_abc():
    length = request.values.get('length', '0')
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
    return f'''
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    <title>Whoami</title>
  </head>
  <body>

    <!-- Option 2: Separate Popper and Bootstrap JS -->

    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>

<form>

    <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label">Length</label>
            <input class="form-control form-control-lg" type="number" name="length" value="{length}" aria-describedby="Help">
            <div id="Help" class="form-text">Input number of random symbols that you want to generate!</div>
    </div>
    <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label">Specials</label>
            <input class="form-control" type="number" name="specials" value="{specials}" aria-describedby="Help">
            <div id="Help" class="form-text">Input 1 if you want to include specials !</div>
    </div>
    <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label">Digits</label>
            <input class="form-control form-control-sm" type="number" name="digits" value="{digits}" aria-describedby="Help">
            <div id="Help" class="form-text">Input 1 if you want to include digits !</div>
    </div>

            {random_choice} <br/>
        <button type="submit" class="btn btn-danger">OK</button>    

</form>
 </body>
   <a href="/"> Home </a>
</html>
'''


@app.route('/')
def main():
    return '''
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    <title>Hello, My First Page :)</title>
  </head>
  <body>
    <h1>My First Page :)</h1>

    <!-- Option 2: Separate Popper and Bootstrap JS -->

    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>

    <div class="container">
      <div class="row">
        <div class="col">
          <a href="/whoami/" id="Colors">
        <img src="https://maindoor.at.ua/_ld/1/96750693.jpg" width="400" height="500" alt="Whoami"/> <br/>
        Whoami </a> <br/>
        </div>
        <div class="col">
          <a href="source_code"id="Colors"> 
        <img src="https://m.media-amazon.com/images/I/51ZXpfWRTwL._SY445_.jpg" width="400" height="500" alt="Source"/> <br/>
        Source code </a> <br/>
        </div>
        <div class="col">
          <a href="/random/"id="Colors">
        <img src="https://m.media-amazon.com/images/M/MV5BMTQ0MTg3NDQ3OV5BMl5BanBnXkFtZTgwODA2MTcxMTE@._V1_FMjpg_UX1000_.jpg" width="400" height="500" alt="Random"/> <br/>
        Random </a> <br/>
        </div>
      </div>
    </div>

  </body>
</html>

'''


app.run('0.0.0.0', debug=True)
