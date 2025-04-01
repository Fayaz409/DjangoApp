from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    print("Home view called")
    return render(request, 'apiapp/home.html')

def builtInFiltersDemo(request):


    print("Built-in filters view called")
    Processors=[
        {"name":"Ryzen 5 5600X","cores":"32"},
        {"name":"Ryzen 5 5600G","cores":"16"},
        {"name":"Ryzen 7 5800X","cores":"32"},
        {"name":"Ryzen 7 5800G","cores":"16"},
        {"name":"Ryzen 9 5900X","cores":"32"},
        {"name":"Ryzen 9 5900G","cores":"16"},
        {"name":"Ryzen 9 5950X","cores":"32"},
        {"name":"Ryzen 9 5950G","cores":"16"}
    ]
    dict_ = {
    "ProbationPeriod": 4,
    "FirstName": "Connors",
    "LastName": "McGregor",
    "PayForFight": 100000,
    "FirstQuarter": ["Jan", "Feb", "Mar"],
    "SecondQuarter": ["Apr", "May", "Jun"],
    "FQuarter": [1, 2, 3],
    "SQuarter": [4, 5, 6],
    "AboutMe": "I am Notorious and I am Ruthless too",
    "now": datetime.datetime.now(),
    "PreviousFight": "",
    "NextFight": None,
    "Processors": Processors,
    "Message": "<h1>I am using escape</h1>",
    "WebSite": "https://www.uiacademy.co.in"
  }
    return render(request, 'apiapp/builtInFilters.html',dict_)


def TestStaticFiles(request):
    return render(request,"apiapp/TSF.html")