from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
# Create your views here.


def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}
    return render(request, 'first_app/index1.html', context=date_dict)


def about(request):
    return HttpResponse("About Pages")
