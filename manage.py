import os
from flask_script import Manager, Server

from appname import create_app

env = os.environ.get('APPNAME_ENV', 'dev')
app = create_app('appname.settings.%sConfig' % env.capitalize())

manager = Manager(app)
manager.add_command("server", Server())

if __name__ == "__main__":
    manager.run()
