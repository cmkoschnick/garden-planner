from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    page_data = {"rows": [
	{"a8": "&#9820" , "b8": "&#9822", "c8":"&#9821", "d8":"&#9819", "e8":"&#9818", "f8":"&#9821", "g8":"&#9822", "h8":"&#9820"},
	{"a7":"&#9823", "b7":"&#9823", "c7":"&#9823", "d7":"&#9823", "e7":"&#9823", "f7":"&#9823", "g7":"&#9823", "h7":"&#9823"},
	{"a6":"&nbsp", "b6":"&nbsp", "c6":"&nbsp","d6":"&nbsp","e6":"&nbsp","f6":"&nbsp","g6":"&nbsp","h6":"&nbsp",},
	{"a5":"&nbsp", "b5":"&nbsp", "c5":"&nbsp","d5":"&nbsp","e5":"&nbsp","f5":"&nbsp","g5":"&nbsp","h5":"&nbsp",},
	{"a4":"&nbsp", "b4":"&nbsp", "c4":"&nbsp","d4":"&nbsp","e4":"&nbsp","f4":"&nbsp","g4":"&nbsp","h4":"&nbsp",},
	{"a3":"&nbsp", "b3":"&nbsp", "c3":"&nbsp","d3":"&nbsp","e3":"&nbsp","f3":"&nbsp","g3":"&nbsp","h3":"&nbsp",},
	{"a2":"&#9817", "b2":"&#9817", "c2":"&#9817", "d2":"&#9817", "e2":"&#9817", "f2":"&#9817", "g2":"&#9817", "h2":"&#9817"},
	{"a1":"&#9814", "b1":"&#9816", "c1":"&#9815", "d1":"&#9813", "e1":"&#9812", "f1":"&#9815", "g1":"&#9816", "h1":"&#9814"}
	]}
    return render(request, 'app1/home.html', page_data)
    
def history(request):
    return render(request, 'app1/history.html')
    
def summary(request):
    return render(request, 'app1/summary.html')
    
def about(request):
    return render(request, 'app1/about.html')
