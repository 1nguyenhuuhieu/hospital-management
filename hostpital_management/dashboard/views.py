from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
# Thư viện kết nối sqlserver
from .sqlserver import sql_server
from .sqlserver import home_query

# Create your views here.
def index(request):
    con = sql_server.get_db()
    if con:
        is_connect_sqlserver = True
        cursor = con.cursor()

        if request.method == 'GET':
            if 'time' in request.GET:
                print(request.GET['time'])
        context = {
        'is_connect_sqlserver': is_connect_sqlserver,
        'value': None
        }
        if is_connect_sqlserver:con.close()
        return render(request, 'dashboard/index.html', context)
    else:
        is_connect_sqlserver = False

