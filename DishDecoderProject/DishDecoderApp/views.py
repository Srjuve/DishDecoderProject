from django.shortcuts import render
from django.http import HttpResponse,HttpResponseForbidden,HttpResponseBadRequest,HttpResponseNotAllowed,HttpResponseNotFound
from .models import *
from .forms import *
# Create your views here.

def main_url(req):
    return HttpResponse('PlaceHolder')