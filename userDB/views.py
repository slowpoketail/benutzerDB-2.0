from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from . import models

@login_required
def index(request):
    return render(request, "index.html")


class SSHKeyView(ListView):
    queryset = models.SSHKey.objects.all()
    template_name = 'sshkey_list.html'


class MACAddressView(ListView):
    queryset = models.MACAddress.objects.all()
    template_name = 'macaddress_list.html'
