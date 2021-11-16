from database import db

class Box(db.Model):

    __tablename__='box'
    id=db.Column('id',db.Integer, primary_key=True, autoincrement=True)
    deck_id= db.Column('deck_id',db.Integer, db.ForeignKey("decks.id"))
    card_id=db.Column(db.Integer, db.ForeignKey("card.id"))


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_cred = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)


class Decks(db.Model):
    __tablename__ = 'decks'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    deck_user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"),nullable=False)
    deck_name = db.Column(db.String, unique=True, nullable=False)
    deck_description = db.Column(db.String)
    deck_score = db.Column(db.Integer)
    deck_last_review_score=db.Column(db.Integer)
    deck_last_review_time=db.Column(db.Integer)
    cards=db.relationship('Box',backref='cards', lazy=True)



class Card(db.Model):
    __tablename__ = 'card'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    card_question = db.Column(db.String, nullable=False)
    card_ans = db.Column(db.String,nullable=False)
    card_notes = db.Column(db.String)
    card_rev_time = db.Column(db.Integer    )
    card_score=db.Column(db.Integer)
    decks=db.relationship('Box',backref='decks',lazy=True)



class Scores(db.Model):
    __tablename__ = 'scores'
    score_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    card_id = db.Column(db.Integer, db.ForeignKey("card.user_id"))
    card_score = db.Column(db.Integer)

