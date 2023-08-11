from sqlalchemy import create_engine,text

engine=create_engine("sqlite:///weefo.db",echo=True)

with engine.connect() as connection:
    result = connection.execute(text('select "hello"'))
    print(result.all())