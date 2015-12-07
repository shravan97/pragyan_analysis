from sqlalchemy import create_engine , Integer , String , Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, TEXT, TINYINT, VARCHAR ,INTEGER , TIMESTAMP , ENUM
from sqlalchemy.orm import sessionmaker

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

class form_elementdata(Base):
	"""for table form_elementdata"""
	__tablename__='form_elementdata'
	__table_args__ = {  
        'mysql_engine': 'InnoDB',  
        'mysql_charset': 'utf8'  
	}
	user_id=Column(INTEGER(11) , nullable=False , primary_key=True , default=0)
	page_modulecomponentid=Column(INTEGER(11) , nullable=False , default=0)
	form_elementid=Column(INTEGER(11) , nullable=False , default=0)
	form_elementdata=Column(TEXT , nullable=False , default=0)
    
class form_elementdesc(Base):
    """for table form_elementdesc"""
    __tablename__='form_elementdesc'
    __table_args__ = {  
        'mysql_engine': 'InnoDB',  
        'mysql_charset': 'utf8'  
    }
    page_modulecomponentid=Column(INTEGER(11) , nullable=False , primary_key=True , default=0)
    form_elementid=Column(INTEGER(11) , nullable=False , default=0)
    form_elementname=Column(VARCHAR(1000) , nullable=False)
    form_elementdisplaytext=Column(VARCHAR(5000) , nullable=False)
    form_elementtype=Column(ENUM('text','textarea','radio','checkbox','select','password','file','date','datetime','member') , nullable=False , default='text')
    form_elementsize=Column(INTEGER(11))
    form_elementtypeoptions=Column(TEXT)
    form_elementdefaultvalue=Column(VARCHAR(4000))
    form_elementmorethan=Column(VARCHAR(4000))
    form_elementlessthan=Column(VARCHAR(4000))
    form_elementcheckint=Column(TINYINT(1) , nullable=False , default=0)
    form_elementtooltiptext=Column(TEXT , nullable=False)
    form_elementisrequired=Column(TINYINT(1) , nullable=False , default=0)
    form_elementrank=Column(INTEGER(11) , nullable=False , default=0)

Session = sessionmaker()
Session.configure(bind=engine)
my_session = Session()
query_chck = my_session.query(form_elementdata).where(page_modulecomponentid=0).all()
print len(query_chck)
#print str(query_chck)