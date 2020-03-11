from django.shortcuts import render

def index (request):
    return render(request,'index.html')


def cal(request):

    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])

    var = request.GET['sign']

    if 'add' in var:
        res = val1+val2
    elif 'sub' in var:
        res = val1-val2
    elif 'mul' in var:
        res = val1*val2
    elif 'div' in var:
        res = val1/val2




    return render(request, 'return.html', {'result': res})
