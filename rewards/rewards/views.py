import operator
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

points1 = [{"payer": "DANNON", "points": 1500, "timestamp": "2022-05-00:30Z"},
               {"payer": "MILLER", "points": 500, "timestamp": "2021-12-29Z"},
               {"payer": "DANNON", "points": 700, "timestamp": "2022-01-18Z"},
               {"payer": "UNILEVER", "points": 2000, "timestamp": "2022-05-13Z"},
               {"payer": "UNILEVER", "points": 300, "timestamp": "2021-11-30Z"},
               {"payer": "DANNON", "points": 500, "timestamp": "2021-09-18Z"},
               {"payer": "MILLER", "points": 1000, "timestamp": "2022-04-23Z"},
               {"payer": "UNILEVER", "points": 450, "timestamp": "2021-10-31Z"},
               {"payer": "DANNON", "points": 250, "timestamp": "2022-02-27Z"},
               {"payer": "UNILEVER", "points": 2000, "timestamp": "2022-02-01Z"},         
               
]

#VIEWS:
def payer_points(request):
    #points1.sort(key = operator.itemgetter('payer','timestamp'))
    #return HttpResponse ("result", str(points1))
    return HttpResponse("These are all the rewards points for every user: ") #error response

def all_points(request):
    ordered_points = (sorted(points1, key = operator.itemgetter('payer', 'timestamp')))
    del_key = 'timestamp'
    for items in ordered_points:
        if del_key in items:
            del items[del_key]
    return HttpResponse(ordered_points)
  
    
        
       
    #  if payer == 'DANNON':
    #         return HttpResponse("You have {points} points available")
    #  elif payer == 'MILLER':
    #     return HttpResponse("You have {points} points available")
    #  elif payer == "UNILEVER":
    #    return HttpResponse("You have {points} points available")
    #  else:
    #     return HttpResponseNotFound("Sorry, account not found") #error response
    
#     return HttpResponse()

# def use_points(request):
#     pass

# def new_point_balance(request):
#     pass
