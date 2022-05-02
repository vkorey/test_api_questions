import sqlalchemy

metadata = sqlalchemy.MetaData()


questions_table = sqlalchemy.Table(
    'questions',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('question_id', sqlalchemy.Integer, unique=True),
    sqlalchemy.Column(
        'question', sqlalchemy.String(40),
        unique=True,
        index=True
    ),
    sqlalchemy.Column('answer', sqlalchemy.String(100)),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime()),
)
