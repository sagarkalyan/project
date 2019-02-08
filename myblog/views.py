from django.shortcuts import render, get_object_or_404
from .models import myblog
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    myblogs=myblog.objects
    return render(request, 'myblogs/index.html',{'myblogs':myblogs})

def detail(request, myblog_id):
    myblog_detail=get_object_or_404(myblog, pk=myblog_id)
    return render(request,'myblogs/detail.html',{'myblog':myblog_detail})


#def blogs(request):
#    myblogs=myblog.objects
#    return render(request, 'myblogs/blogs.html',{'myblogs':myblogs})

def blogs(request):
    myblogg = myblog.objects.all()
    paginator = Paginator(myblogg, 4) # Shows 4 posts per page
    page = request.GET.get('page')
    myblogs = paginator.get_page(page)
    return render(request, 'myblogs/blogs.html', {'myblogs': myblogs})


def about(request):
    myblogs=myblog.objects
    return render(request, 'myblogs/about-me.html',{'myblogs':myblogs})

# Purpose to add this: added pagination page to check if its working properly or not.
def pagination(request):
    myblogg = myblog.objects.all()
    paginator = Paginator(myblogg, 2) # Show 25 contacts per page
    page = request.GET.get('page')
    myblogs = paginator.get_page(page)
    return render(request, 'myblogs/pagination.html', {'myblogs': myblogs})
