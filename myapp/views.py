from django.shortcuts import render
from .models import Post  # New
# Create your views here.

    # Query all posts



from django.shortcuts import render
from .models import Post  # New
from django.db.models import Q  # New
# Create your views here.
def index(request):
    # Query all posts
    search_post = request.GET.get('search')
    posts = Post.objects.all()
    if search_post:
        posts = Post.objects.filter(Q(title__icontains=search_post) & Q(content__icontains=search_post))
    else:
        posts = Post.objects.all().order_by("-date_created")

    return render(request, 'myapp/index.html', {'posts': posts})
