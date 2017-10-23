from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,Topic, Webpage

# Create your views here.

def index(request):
    webpg_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpg_list}
    my_dict={"insert_me":"Hello how are you, I am from view.py"}
    return render(request, "first_app/index.html", context=date_dict)
