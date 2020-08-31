from .. import db

class MyTable(db.Model):
    __tablename__ = 'MY_TABLE'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    test = db.Column(db.String(255), nullable=False)
    
    @property
    def serialize(self):
        return {
            'id':self.id,
            'test':self.test
        }

    def __repr__(self):
        return f"<MyTable {self.test}>"