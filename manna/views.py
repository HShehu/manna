from django.shortcuts import render
from .models import Project, Phone_No, Email, Account
from django.views.generic import ListView,DetailView
# Create your views here.

accounts = Account.objects.all()
phone_nos = Phone_No.objects.all()
emails = Email.objects.all()

def home(request):

    return render(request, 'manna/home.html')


def get_in_touch(request):

    context = {
        'phone_nos': phone_nos,
        'emails': emails
    }

    return render(request, 'manna/get_in_touch.html', context)


def how_you_can_help(request):
    context = {
        'accounts': accounts,
    }
    return render(request, 'manna/how_you_can_help.html', context)


class ProjectListView(ListView):
    model = Project
    template_name ="manna/what_we_do.html"
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project