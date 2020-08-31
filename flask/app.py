import os
from api_v1 import create_app, db
from api_v1.main.models import *

app = create_app(os.getenv('PROJECT_CONFIG') or 'default')

@app.shell_context_processor
def make_shell_context():
    return dict(
        db=db,
        MyTable=MyTable
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


