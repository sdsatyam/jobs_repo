from django.shortcuts import render
from testapp.models import HydJobs,PuneJobs,BangJobs
# Create your views here.
def homepage_view(request):
    return render(request,'testapp/index.html')

def hydjobs_view(request):
    jobs_list=HydJobs.objects.all()
    type='hydjobs'
    my_dict={'jobs_list':jobs_list,'type':type}
    return render(request,'testapp/jobs1.html',my_dict)

def punejobs_view(request):
    jobs_list=PuneJobs.objects.all()
    type='punejobs'
    my_dict={'jobs_list':jobs_list,'type':type}
    return render(request,'testapp/punejob.html',my_dict)

def bangjobs_view(request):
    jobs_list=BangJobs.objects.all()
    type='bangjobs'
    my_dict={'jobs_list':jobs_list,'type':type}
    return render(request,'testapp/bangjobs.html',my_dict)

