from django.http import HttpResponse
import os

# Create your views here.

def index(request):
	html = "<p>Hello World!</p>"
	return HttpResponse(html)

def log(request):
	log ="<h1>/var/log/ directory conent is: </h1>"
	for filename in os.listdir("/var/log/"):
		log+="<br>"+filename+"\n"
	return HttpResponse(log)

def apt(request):
	apt =""
	for filename in os.listdir("/var/log/apt/"):
	    apt+=filename+"<br>"
	return HttpResponse(apt)
