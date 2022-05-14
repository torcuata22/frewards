import operator
from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

points1 = [{"payer": "DANNON", "points": 1500, "timestamp": "2022-05-00:30Z"},
               {"payer": "MILLER COORS", "points": 500, "timestamp": "2021-12-29Z"},
               {"payer": "DANNON", "points": 700, "timestamp": "2022-01-18Z"},
               {"payer": "UNILEVER", "points": 2000, "timestamp": "2022-05-13Z"},
               {"payer": "", "points": 300, "timestamp": "2021-11-30Z"},
               {"payer": "DANNON", "points": 500, "timestamp": "2021-09-18Z"},
               {"payer": "MILLER COORS", "points": 1000, "timestamp": "2022-04-23Z"},
               {"payer": "UNILEVER", "points": 450, "timestamp": "2021-10-31Z"},
               {"payer": "DANNON", "points": 250, "timestamp": "2022-02-27Z"},
               {"payer": "UNILEVER", "points": 2000, "timestamp": "2022-02-01Z"},         
               
]

#VIEWS:
def show_payer_points(request):
    points1.sort(key = operator.itemgetter('payer','timestamp'))
print ("result", str(points1))

def available_points(request):
    pass






'''
def index(request): 
    points = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    }) 

def challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        raise Http404
    else:
        redirect_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month]) #builds path that looks like this: /challenge/<redirect_month>, which is why we use args = redirect_month as the second parameter
        return HttpResponseRedirect(redirect_path)
    

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render (request,"challenges/challenge.html", {
            "text": challenge_text , 
            "month_name": month   
        })
    except:
         raise Http404()
         
         desired output:
         spend points with the request: {"points": 5000}
         spend points (older ones first), and return:
         new_points = {"payer": NAME, "points": points left}
         
         '''