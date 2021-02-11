from django.shortcuts import render, HttpResponse
# HttpResponse vai interpretrar o que jogar como parametro e jogar para http

# Create your views here.

def hello(request, nome):
    return HttpResponse('<h1>Hello {}<h1/>'.format(nome))

