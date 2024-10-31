from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome(request):
    return HttpResponse('<h1>Welcome to Django Om namha shivay web-application!</h1>')

def temp(request):
    return HttpResponse('<h1>Om bhur bhuvsvha tasvitur varenyam bhargodevasya dhimahi dhiyoyo... maha prachodayat om........om......</h1>')

def loan_roi(request):
    return HttpResponse('<h1>this is loan related information</h1>')