from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

# Create your views here.
# def aboutUs(request):
#     return render(request, "about_us/index.html")



class AboutUsView(TemplateView):

    """Environ View Definition"""

    template_name = "about_us.html"