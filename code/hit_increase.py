import httplib
for i in range(0,10000):
	conn = httplib.HTTPConnection("www.hit-counter-html-code.com")
	conn.request("GET","/c.php?d=9&id=128788&s=8")
	r1=conn.getresponse()
	print r1.status
	data=r1.read()
	r1.close()
