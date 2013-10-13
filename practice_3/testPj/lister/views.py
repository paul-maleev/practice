from django.http import HttpResponse
import os, time

# Create your views here.

def index(request):
	html = "<p>Hello World!</p>"
	return HttpResponse(html)

def log(request):
	filepath = "/var/log/"
	log="<h1>"+filepath+" directory content is: </h1>"
	log+="<table border=1>"
	log+="<tr><td><b>File name</b></td><td><b>File size</b></td><td><b>Last modifcation date</b></td></tr>"
		
	for filename in os.listdir(filepath):
		size=os.path.getsize(os.path.join(filepath,filename))
		last_mod=time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(os.path.getmtime(os.path.join(filepath,filename))))
		log+="<tr>"		
		if os.path.isfile(os.path.join(filepath,filename)):
			log+="<td>"+filename+"</td><td>"+str(size)+"</td><td>"+last_mod+"</td>"
		else:
			log+="<td><a href=\"./"+filename+"\">./"+filename+"</a>"+"</td><td>"+str(size)+"</td><td>"+last_mod+"</td>"
		log+="</tr>"
	log+="</table>"
	return HttpResponse(log)

def apt(request):
	filepath = "/var/log/apt/"
	apt ="<h1>"+filepath+" directory content is: </h1>"
	apt+= "<table border=1>"
	apt+= "<tr><td><b>File name</b></td><td><b>File size</b></td><td><b>Last modifcation date</b></td></tr>"	
	for filename in os.listdir(filepath):
		size=os.path.getsize(os.path.join(filepath,filename))
		last_mod=time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(os.path.getmtime(os.path.join(filepath,filename))))
		apt+="<tr>"		
		if os.path.isfile(os.path.join(filepath,filename)):
			apt+="<td>"+filename+"</td><td>"+str(size)+"</td><td>"+last_mod+"</td>"
		else:
			apt+="<td><a href=\"./"+filename+"\">./"+filename+"</a>"+"</td><td>"+str(size)+"</td><td>"+last_mod+"</td>"
		apt+="</tr>"
	apt+="</table>"
	return HttpResponse(apt)
