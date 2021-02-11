from django.shortcuts import render, HttpResponse
# HttpResponse vai interpretrar o que jogar como parametro e jogar para http

# Create your views here.

def hello(request, nome):
    return HttpResponse('<h1>Hello {}<h1/>'.format(nome))

def operacoes(request, operacao,  num1, num2):
    if operacao == '+':
        return HttpResponse('<h1>A soma de {} + {} = {}<h1/>'.format(num1, num2, (num1+num2)))
    elif operacao == '-':
        return HttpResponse('<h1>A soma de {} + {} = {}<h1/>'.format(num1, num2, (num1-num2)))
    elif operacao == ':':
        return HttpResponse('<h1>A soma de {} + {} = {}<h1/>'.format(num1, num2, (num1/num2)))
    elif operacao == '*':
        return HttpResponse('<h1>A soma de {} + {} = {}<h1/>'.format(num1, num2, (num1*num2)))
    else:
        return HttpResponse('<h1>Operação invalida >> {} << <h1/>'.format(operacao))
