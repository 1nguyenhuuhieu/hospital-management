from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
# Thư viện kết nối sqlserver
import pyodbc
from dashboard.app.sqlserver import *


# Create your views here.


def index(request):
    f = sql_server.get_db()
    context = {

    }
    return render(request, 'dashboard/index.html', context)