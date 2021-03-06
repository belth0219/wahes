from django.template.loader import get_template
from django.http import HttpResponse
from datetime import datetime
from .models import Post

# Create your views here.
def homepage(request):
    post = Post.objects.all()
    post_lists = list()
    for count, post in enumerate(post):
        post_lists.append("No.{}:".format(str(count)) + str(post) + "<br>")
        post_lists.append("<small>" + str(post.body) + "</small><br><br>")
    return HttpResponse(post_lists)
