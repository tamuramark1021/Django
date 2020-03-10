from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context={
        "score": "current_score",
    }
    return render(request, "index.html", context)