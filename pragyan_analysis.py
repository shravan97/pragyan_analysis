from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , scoped_session
import time , os
import getpass

# host = raw_input("Enter the host name : ")
# u_id = raw_input("Enter your mysql username : ")
# pwd = getpass.getpass()

engine = create_engine('mysql://<mysql_username>:<mysql_password>@<mysql_host>/<database>')
Session = scoped_session(sessionmaker(bind=engine))
my_session = Session()

result = my_session.execute("SELECT `page_modulecomponentid` , `page_parentid` FROM `pragyanV3_pages` WHERE `page_name` LIKE 'registration' AND  `page_module` LIKE 'form';").fetchall()

curr_dir = os.getcwd()

f_degree = open(curr_dir + '/analysis1.txt' , 'w')
f_institute = open(curr_dir + '/analysis2.txt' , 'w')


for k in range(len(result)):
	
	#result_form = my_session.execute("SELECT `form_elementid` , `form_elementname` FROM `form_elementdesc` WHERE `page_modulecomponentid`="+ str(result[k][1]) +";").fetchall()
	
	#print len(result_form)
	
	res1 = my_session.execute("SELECT `page_name` from pragyanV3_pages where page_id="+str(result[k][1])+";").fetchall();
	if str(result[k][1])=='25' or str(result[k][1])=='47':
		continue

	f_degree.write(res1[0][0] +'\n\n')
	f_institute.write(res1[0][0] +'\n\n')

	#result_form_data = my_session.execute("SELECT `form_elementdata` FROM `form_elementdata` WHERE `page_modulecomponentid`="+str(result[k][0])+";").fetchall()
	#The above query gets the year of student . This has to be done for all form attributes
	#0,1,4,6,9,10,13,
	res2 =my_session.execute("SELECT distinct(user_id) from form_elementdata where page_modulecomponentid ="+str(result[k][0])+" ;").fetchall() 
	arr_users = [(int)(i[0]) for i in res2]

	res3=my_session.execute("SELECT form_elementdata  from form_elementdata where page_modulecomponentid ="+str(result[k][0])+" and form_elementdata REGEXP '^-?[0-9]+$' and CHAR_LENGTH(form_elementdata)=6 group by form_elementdata;").fetchall()
	arr_team_members = [(int)(i[0]) for i in res3]

	arr = arr_users + arr_team_members
	arr=list(set(arr))
	lvl={}
	inst={}

	for r_num in arr:
		res4=my_session.execute("SELECT form_elementdata from form_elementdata where user_id="+str(r_num)+" and form_elementid=7;").fetchall();
		res_institute = my_session.execute("SELECT form_elementdata from form_elementdata where user_id="+str(r_num)+" and form_elementid=10;").fetchall()

		if res_institute:
			if res_institute[0][0] in inst and res_institute[0][0]!='':
				inst[res_institute[0][0]]+=1
			elif res_institute[0][0]!='':
				inst[res_institute[0][0]]=1	

		if res4:
		  if res4[0][0] in lvl and res4[0][0]!='':
		  	lvl[res4[0][0]]+=1
		  elif res4[0][0]!='':
		  	lvl[res4[0][0]]=1
	
	sum_vals=0
	sum_vals_1=0  	
	for x in lvl:
		sum_vals+=lvl[x]

	for x in inst:
		sum_vals_1+=inst[x]

	for k in lvl :
		f_degree.write(k+"  :  " +str(lvl[k])+'\n\n')
	

	for k in inst :
		f_institute.write(k+"  :  "+str(inst[k])+'\n\n')


	f_degree.write("Total  :  "+str(len(arr)) + '\n\n')
	f_institute.write("Total  :  "+str(len(arr))+'\n\n')

	if sum_vals!=len(arr):
	 	f_degree.write("("+str(len(arr)-sum_vals)+" of their levels of study were not listed)"+'\n\n')

	if sum_vals_1!=len(arr):
	 	f_institute.write("("+str(len(arr)-sum_vals_1) + " of their institutes were not listed)" + '\n\n')


	f_degree.write('No. of teams registered :  '+str(len(arr_users)))
	f_institute.write('No. of teams registered :  '+str(len(arr_users))) 	


	f_degree.write('\n\n\n\n')
	f_institute.write('\n\n\n\n') 		



	""" flag=0
	
	for i in arr :
		result_form_data = my_session.execute("SELECT count(form_elementdata) , `form_elementdata` FROM `form_elementdata` WHERE `page_modulecomponentid`=0 AND `form_elementid`="+str(i)+" GROUP BY form_elementdata;").fetchall()
		os.system('clear')
		for j in result_form_data :
			print j[1] , " : " , j[0]
		time.sleep(5) 
	"""
f_degree.close()
f_institute.close()	
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
add queries
"""