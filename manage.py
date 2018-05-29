
from flask_script import Manager,Server
from app import create_app,db
from app.models import User

app = create_app('default')

manager = Manager(app)

manager.add_command('server', Server)

@manager.shell
def make_shell_context():
    return dict(app=app, User=User)

if __name__ == '__main__':
    manager.run()

