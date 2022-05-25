from http.client import PAYMENT_REQUIRED
import operator
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
import json

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

#VIEWS


def home(request):
      return render(request, "index.html") #works!
  
def points(request):
   return render(request, 'all_points.html')

def payer_points(request):
    pass

def all_points(request):
    points= sorted(points1, key = operator.itemgetter('payer', 'timestamp'))
    return render(request, "all_points.html",{"points": points})

def payer_points(request):
    points= sorted(points1, key = operator.itemgetter('payer', 'timestamp'))
    return render (request, "payer_points.html", {
        "points": points
    })
    
  
  
def d_payer_points(request):
    ordered_points = (sorted(points1, key = operator.itemgetter('payer', 'timestamp')))
    dannon = ordered_points[:3]
    return render(request,"dpayer_points.html",{"dannon": dannon})
    
        
def m_payer_points(request):
     ordered_points = (sorted(points1, key = operator.itemgetter('payer', 'timestamp')))
     miller = ordered_points[4:6]
     return render(request,"mpayer_points.html",{"miller": miller})        
        
        
def u_payer_points(request):
     ordered_points = (sorted(points1, key = operator.itemgetter('payer', 'timestamp')))
     unilever = ordered_points[6:]
     return render(request, 'upayer_points.html', {"unilever": unilever})

def spend_points(request):  
    global points1 
# sort data structure by timestamp, earliest records first 
    earliest_points_sorted = sorted(points1, key=lambda d: d["timestamp"])
    updated_records, spend_diff_response = [], []  # spend points across earliest payers, modify dict in-place
    points_to_spend = 5000

    while points_to_spend > 0:
        loop_num = 0

        for record in earliest_points_sorted:
            
            curr_points = record['points'] 

            if curr_points < points_to_spend: 
                record['points'] = 0 
                points_to_spend += (-1 * curr_points)

            else: 
                record['points'] -= points_to_spend 
                points_to_spend = 0  # track updated records & records for response 
                updated_records.append({"payer": record["payer"], "points": record['points'], "timestamp": record['timestamp']}) 
                spend_diff_response.append({"payer": record["payer"], "points": record['points'] - curr_points})  # if all payers evaluated, break the spend and return remaining points

        loop_num += 1
        if loop_num > 50:
            break
         
    if updated_records != []:
        points1 = updated_records

    updated_records = flatten_updated_records(updated_records)
    spend_diff_response = flatten_updated_records(spend_diff_response)

    
    response_data = f"After using the user's 5000 points, the payer points were updated to:<br>{updated_records}<br><br>Here's the point difference:<br>{spend_diff_response}<br><br>Points left to spend:{points_to_spend}"

    return HttpResponse(response_data)

 
def flatten_updated_records(updated_records): 
    flat_updated_records = [] 
    all_payers = set([x["payer"] for x in updated_records]) 
    for payer in all_payers: # get all points per payer 
        sum_payer_records = [x for x in updated_records if x["payer"] == payer] 
        sum_pts = sum([x["points"] for x in sum_payer_records]) 
        flat_updated_records.append({"payer": payer, "points": sum_pts})  
    
    
    return flat_updated_records

  
  

