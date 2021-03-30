from django.shortcuts import render
from django.http import HttpResponse,HttpResponseForbidden,HttpResponseBadRequest,HttpResponseNotAllowed,HttpResponseNotFound
from .models import *
from .forms import Main_page_form
# Create your views here.

def main_url(req):
    template_name="DishDecoderApp/main_url.html"
    template_data = {}
    if req.method == 'GET':
        form = Main_page_form()
        template_data['form']=form
        template_data['login_button_link']="/login/"
        template_data['search_form_link']="/search/"
        template_data['create_receip_link']="/create/"
        return render(req, template_name,template_data)
    return HttpResponseBadRequest()