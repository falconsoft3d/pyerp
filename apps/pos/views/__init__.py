from django.shortcuts import HttpResponse, render

def PosIndex(request):
    return render(request, 'pos/pos.html')