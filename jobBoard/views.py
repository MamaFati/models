from django.shortcuts import render, get_object_or_404
from .models import jobPosting
# Create your views here.
def index(request):
    # jobs = jobPosting.objects.all()
    active_postings = jobPosting.objects.filter(is_active=True)
    context ={
        'job_postings': active_postings
    }
    return render(request,'jobBoard/index.html', context) 

def job_details(request, pk):
    job_postings = get_object_or_404(jobPosting, pk=pk, is_active=True)
    context ={
        'posting': job_postings
    }
    return render(request,'jobBoard/detail.html',context )