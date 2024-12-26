from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import Post


# Create your views here.
class PostList(generic.ListView):
    # queryset = Post.objects.all()
    # queryset = Post.objects.all().order_by("created_on")
    # queryset = Post.objects.all().order_by("-created_on")
    queryset = Post.objects.filter(status=1)
    template_name = "blog2050/index.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`blog2050.Post`.

    **Context**

    ``post``
        An instance of :model:`blog2050.Post`.

    **Template:**

    :template:`blog2050/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog2050/post_detail.html",
        {"post": post,
         "coder": "Mohamed Mesto"},
    )