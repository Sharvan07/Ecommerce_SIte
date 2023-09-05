from unwrap import app
from unwrap import db
from unwrap.models import User

db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
