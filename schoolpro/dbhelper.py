from django.db import connection

def rfact(cr,r):
	#return{"id":r[0],"item":r[1]}
	return {i[1][0]:r[i[0]] for i in enumerate(cr.description)}

def getdata(sql,single=False):
	rval=[]
	err=None
	c = connection.cursor()
	c.cursor.row_factory=rfact
	try:
		c.execute(sql)
		if single:
			rval = c.fetchone()
		else:
			rval=c.fetchall()
	except Exception as es:
		err=str(es)
		print('error getdata :',err)
	c.close()
	return rval,err

def updatedata(sql,rowid=False):
	rval=None
	err=None
	c = connection.cursor()
	try:
		c.execute(sql)
		if rowid:
			rval =c.lastrowid
		else:
			rval=True
	except Exception as es:
		err=str(es)
		print('error updatedata :',err)
	c.close()
	return rval,err