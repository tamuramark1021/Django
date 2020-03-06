from django.shortcuts import render
from time import gmtime, localtime, strftime, strptime
def index(request):
    context={
        "time": strftime("%I: %M %p", localtime()),
        "date": strftime("%m/ %d/ %Y", gmtime()),

        # "time2": strptime("localtime()", "%H: %M"),
        # "date2": strptime("gmtime()", "%m/ %d/ %Y"),
    }
    return render(request, 'index.html', context)

# def



# Create your views here.
