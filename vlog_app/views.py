from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.db.models.query import QuerySet
from datetime import datetime


from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.
# def index(request):
#     all_post = Post.objects.all()
#     print(all_post)
#     return HttpResponse(f"{all_post[0].description}, {all_post[0].title}, <br><h3>{all_post[0].img}</h3>")


# def summury(request):
#     a = 5
#     b = 4
#     return HttpResponse(f"a + b")



# Create your views here.
def index(request):
    all_post = Post.objects.all()
    context = {
        "all_posts": all_post,
        "test": datetime.now(),
    }
    return render(
        request=request,
        template_name='vlog_app/index.html',
        context=context
        )
    
    
# Model View Controller
# Model Template View
    
    