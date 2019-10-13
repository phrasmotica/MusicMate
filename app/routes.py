from app import app

# home page
@app.route('/')
@app.route('/index')
def index():
    return "Hello, world!"
