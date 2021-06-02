from app import db

class BasicModel():
    def insert(self):
        db.session.add(self)
        try:
            db.session.commit()
            return self
        except Exception as e:
            db.session.rollback()
            raise RuntimeError("Error when inserting new data")

    @staticmethod
    def update():
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise RuntimeError("Error when inserting new data")

    def delete(self):
        db.session.delete(self)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise RuntimeError("Error when inserting new data")
