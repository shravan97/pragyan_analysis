from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , scoped_session
import time , os

engine = create_engine('mysql://root:Lordsvn_97@localhost/dummy')
Session = scoped_session(sessionmaker(bind=engine))
my_session = Session()

result = my_session.execute("SELECT `page_modulecomponentid` , `page_parentid` FROM `pragyanV3_pages` WHERE `page_name` LIKE 'registration' AND  `page_module` LIKE 'form';").fetchall()


for k in range(len(result)):
	
	#result_form = my_session.execute("SELECT `form_elementid` , `form_elementname` FROM `form_elementdesc` WHERE `page_modulecomponentid`="+ str(result[k][1]) +";").fetchall()
	
	#print len(result_form)
	
	res1 = my_session.execute("SELECT `page_name` from pragyanV3_pages where page_id="+str(result[k][1])+";").fetchall();
	print res1[0][0],'\n'

	#result_form_data = my_session.execute("SELECT `form_elementdata` FROM `form_elementdata` WHERE `page_modulecomponentid`="+str(result[k][0])+";").fetchall()
	#The above query gets the year of student . This has to be done for all form attributes
	#0,1,4,6,9,10,13,
	res2 =my_session.execute("SELECT distinct(user_id) from form_elementdata where page_modulecomponentid ="+str(result[k][0])+" ;").fetchall() 
	arr_users = [(int)(i[0]) for i in res2]

	res3=my_session.execute("SELECT form_elementdata  from form_elementdata where page_modulecomponentid ="+str(result[k][0])+" and form_elementdata REGEXP '^-?[0-9]+$'  group by form_elementdata;").fetchall()
	arr_team_members = [(int)(i[0]) for i in res3]

	arr = arr_users + arr_team_members
	arr=list(set(arr))

	for r_num in arr:
		res4=my_session.execute("SELECT form_elementdata from form_elementdata where user_id="+str(r_num)+" and form_elementid=8;").fetchall();
		print res4[0][0]

	print len(arr),'\n'
	time.sleep(3)
	os.system('clear')



	""" flag=0
	
	for i in arr :
		result_form_data = my_session.execute("SELECT count(form_elementdata) , `form_elementdata` FROM `form_elementdata` WHERE `page_modulecomponentid`=0 AND `form_elementid`="+str(i)+" GROUP BY form_elementdata;").fetchall()
		os.system('clear')
		for j in result_form_data :
			print j[1] , " : " , j[0]
		time.sleep(5) 
	"""
#print result_form

#query from line 14 , hence get page_parentid
#consider page_modulecomponentid =1
#select page_name from pragyanV3_pages where page_id=<the page_parentid from query on line 9>;
#select form_elementname  , form_elementid  from form_elementdesc where page_modulecomponentid=1;(not compulsory)
#select distinct(user_id) from form_elementdata where page_modulecomponentid =1 ;<then get the array of user_id s>
#select form_elementdata  from form_elementdata where page_modulecomponentid =1 and form_elementdata REGEXP '[0-9]+' group by form_elementdata;
#from the above query get the array of form_elementdata .
#merge the arrays and then execute arr = list(set(arr))

""" ToDo : 

Get input of mysql uname and pwd and name of host
add queries
"""