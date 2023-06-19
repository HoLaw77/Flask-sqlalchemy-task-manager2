from taskmanager import db


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.Strin(25), unique=True, nullable=False)
    tasks = db.relationship("Task", backref="cateogry",
                            cascade="all, delete", lazy=True)


class task(db.Model):
    # schema for the task model
    id = db.Column(db.integer, primary_key=True)
    task_name = db.Column(db.string(50), unique=True, nullable=False)
    task_description = db.Column(db.text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(
        "category.id",  ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Task: {1} | urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )
