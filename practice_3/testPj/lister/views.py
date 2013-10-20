from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, Template
from django.template.loader import get_template
import os, time, datetime

# Create your views here.


def listing(request, file_path):
    context = {}
    base_path = "/var/log/"
    file_path = base_path + file_path
    for file_name in os.listdir(file_path):
        size = os.path.getsize(os.path.join(file_path, file_name))
        is_file = True
        if os.path.isfile(os.path.join(file_path, file_name)):
            is_file = True
        else:
            is_file = False
        context[file_name] = {'name': file_name, 'fullpath': file_path, 'size': size,
                              'last_mod': time.strftime("%m/%d/%Y %I:%M:%S %p",
                                                        time.localtime(
                                                            os.path.getmtime(
                                                                os.path.join(
                                                                    file_path,
                                                                    file_name)))),
                              'is_file': is_file}
    return render_to_response('listing.html', {'context': context})


def index(request):
    html = "<p>Hello World!</p>"
    return HttpResponse(html)