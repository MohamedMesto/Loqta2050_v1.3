from django.shortcuts import render
from .models import Aboutus


def about_us(request):
    """
    Renders the Aboutus page
    """
    aboutus = Aboutus.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "aboutus/aboutus.html",
        {"aboutus": aboutus},
    )