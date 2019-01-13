from app import create_app, db
from app.models import User, Post

app = create_app()

'''
if __name__ == '__main__':
    debug_mode = True
'''

if __name__ == '__main__':
    app.run(debug=True)



@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}