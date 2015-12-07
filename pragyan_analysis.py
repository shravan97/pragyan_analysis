from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , scoped_session

engine = create_engine('mysql://root:Lordsvn_97@localhost/dummy')
Session = scoped_session(sessionmaker(bind=engine))
my_session = Session()

result = my_session.execute("SELECT * FROM `pragyanV3_pages` WHERE `page_name` LIKE 'registration' AND  `page_module` LIKE 'form';").fetchall()
print len(result)