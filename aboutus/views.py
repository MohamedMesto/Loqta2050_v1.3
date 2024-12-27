from django.shortcuts import render
from .models import Aboutus
from .forms import CollaborateForm


def about_us(request):
    """
    Renders the Aboutus page
    """
    aboutus = Aboutus.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()


    return render(
        request,
        "aboutus/aboutus.html",
        {
            "aboutus": aboutus,
            "collaborate_form": collaborate_form
        },
    )