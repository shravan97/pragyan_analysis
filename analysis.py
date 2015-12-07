from sqlalchemy import create_engine , Integer , String , Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, TEXT, TINYINT, VARCHAR ,INTEGER , TIMESTAMP , ENUM

engine=create_engine('mysql://root:Lordsvn_97@localhost/dummy')

Base = declarative_base()

class pragyanV3_pages(Base):
	"""for table pragyanV3_pages"""
	__tablename__='pragyanV3_pages'
	__table_args__ = {  
        'mysql_engine': 'InnoDB',  
        'mysql_charset': 'utf8'  
    } 
	page_id=Column(INTEGER(11) , nullable=False , primary_key=True , autoincrement=True)
	page_name=Column(VARCHAR(32), nullable=False)
	page_parentid=Column(INTEGER(11) , nullable=False)
	page_createdtime=Column(TIMESTAMP , nullable=False , default='CURRENT_TIMESTAMP')
	page_lastaccesstime=Column(TIMESTAMP , nullable=False , default='0000-00-00 00:00:00')
	page_title=Column(VARCHAR(128), nullable=False , default='New Page')
	page_module=Column(VARCHAR(128), nullable=False)
	page_modulecomponentid=Column(Integer , nullable=False)
	page_template=Column(VARCHAR(50) , nullable=False)
	page_image=Column(VARCHAR(300))
	page_menurank=Column(INTEGER(11) , nullable=False)
	page_inheritedinfoid=Column(INTEGER(11) , nullable=False , default= -1)
	page_displayinmenu=Column(TINYINT(1) , nullable=False , default=1)
	page_displayinsitemap=Column(TINYINT(1) , nullable=False , default=1)
	page_displaymenu=Column(TINYINT(1) , nullable=False , default=1)
	page_displaysiblingmenu=Column(TINYINT(1) , nullable=False , default=1)
	page_displaypageheading=Column(TINYINT(1) , nullable=False , default=1)
	page_displayicon=Column(TINYINT(1) , nullable=False , default=1)
	page_menutype=Column(ENUM('classic', 'complete', 'multidepth') , nullable=False , default='classic')
	page_menudepth=Column(INTEGER(11) , nullable=False , default=1)
	page_openinnewtab=Column(TINYINT(1) , nullable=False , default=0)

class form_elementdata(object):
	"""for table form_elementdata"""
	__tablename__='form_elementdata'
	__table_args__ = {  
        'mysql_engine': 'InnoDB',  
        'mysql_charset': 'utf8'  
    }
    user_id=Column(INTEGER(11) , nullable=False , default=0 , primary_key=True)
    page_modulecomponentid=Column(INTEGER(11) , nullable=False , default=0)
    form_elementid=Column(INTEGER(11) , nullable=False , default=0)
    form_elementdata=Column(TEXT , nullable=False , default=0)
    