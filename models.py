from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    Bookings = db.relationship('Bookings', backref='user', lazy=True)
    car_reserved = db.relationship('Cars', backref='car_reserved', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Bookings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_start = db.Column(db.DateTime, nullable=False)
    date_end = db.Column(db.DateTime, nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Books('{self.date_start}', '{self.date_end}', '{self.car_id}', '{self.user_id}')"


class Cars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car = db.Column(db.String(20), nullable=False)
    car_description = db.Column(db.Text(500), nullable=False)
    car_price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Car('{self.car}', '{self.car_price}')"
