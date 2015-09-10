from django.shortcuts import render,render_to_response
#from django.http import HttpResponse
from .models import Blog
# Create your views here.
def show(request):
    
    #SELECT * FROM blogs
    blogs=Blog.objects.all()
    '''resp=''
    print(blogs)
    for blog in blogs:
        print('='*72)
        print(blog)
        resp+=blog.content+'----------'

    return HttpResponse(resp)
    '''
    return render_to_response('show.html',{'blogs':blogs})