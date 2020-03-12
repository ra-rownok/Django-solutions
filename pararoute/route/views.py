from django.shortcuts import render


# Create your views here.
def sum(request, num1, num2):
    res = num1 + num2
    return render(request, 'index.html', {'result': res})


def sub(request, num1, num2):
    res = num1 - num2
    return render(request, 'index.html', {'result': res})
