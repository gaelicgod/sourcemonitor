from flask import Flask
app = Flask(__name__)

projects = [
    'sanlam_reality2',
    'redbull-editions',
    'mlp',
    'zoo',
]

@app.route('/')
def index():
    return 'Index Page!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

def do_the_login():
    pass

def show_the_login_form():
    pass


if __name__ == '__main__':
    app.debug = True
    app.run()
