from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , scoped_session

engine = create_engine('mysql://root:Lordsvn_97@localhost/dummy')
Session = scoped_session(sessionmaker(bind=engine))
my_session = Session()

result = my_session.execute("SELECT `page_modulecomponentid` FROM `pragyanV3_pages` WHERE `page_name` LIKE 'registration' AND  `page_module` LIKE 'form';").fetchall()

result_form = my_session.execute("SELECT `form_elementid` , `form_elementname` FROM `form_elementdesc` WHERE `page_modulecomponentid`=0;").fetchall()
#The above query is for registration page at pragyan site


result_form_data = my_session.execute("SELECT `form_elementdata` FROM `form_elementdata` WHERE `page_modulecomponentid`=0 AND `form_elementid`=9;").fetchall()
#The above query gets the year of student . This has to be done for all form attributes

print result_form

""" ToDo : 

Get input of mysql uname and pwd and name of host
add queries
"""
