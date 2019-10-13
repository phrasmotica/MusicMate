from app import app, db
from app.models import User, Review

# allow us to run 'flask shell' and have all the imports we need from the get-go
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Review': Review}
