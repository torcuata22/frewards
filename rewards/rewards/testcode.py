import operator
from collections import defaultdict
from itertools import groupby
import json

points1 = [{"payer": "DANNON", "points": 1500, "timestamp": "2022-05-30Z"},
               {"payer": "MILLER COORS", "points": 500, "timestamp": "2021-12-29Z"},
               {"payer": "DANNON", "points": 700, "timestamp": "2022-01-18Z"},
               {"payer": "UNILEVER", "points": 2000, "timestamp": "2022-05-13Z"},
               {"payer": "MILLER COORS", "points": 300, "timestamp": "2021-11-30Z"},
               {"payer": "DANNON", "points": 500, "timestamp": "2021-09-18Z"},
               {"payer": "MILLER COORS", "points": 1000, "timestamp": "2022-04-23Z"},
               {"payer": "UNILEVER", "points": 450, "timestamp": "2021-10-31Z"},
               {"payer": "DANNON", "points": 250, "timestamp": "2022-02-27Z"},
               {"payer": "UNILEVER", "points": 2000, "timestamp": "2022-02-01Z"},         
               
]
points_to_spend = 5000
    
def spend_points(points1, points_to_spend):

# sort data structure by timestamp, earliest records first   
    
    earliest_points_sorted = sorted(points1, key=lambda d: d["timestamp"])  
    updated_records, spend_diff_response = [], []  # spend points across earliest payers, modify dict in-place
    
    while points_to_spend > 0: 
        for record in earliest_points_sorted:   
            curr_points = record['points']  

        if curr_points < points_to_spend: 
            record['points'] = 0 
            points_to_spend += (-1 * curr_points) 
            
        else: 
            record['points'] -= points_to_spend 
            points_to_spend = 0  # track updated records & records for response 
            updated_records.append({"payer": record["payer"], "points": record['points']}) 
            spend_diff_response.append({"payer": record["payer"], "points": record['points'] - curr_points})  # if all payers evaluated, break the spend and return remaining points

        if record == earliest_points_sorted[-1]: 
            break  

    updated_records = flatten_updated_records(updated_records) 
    spend_diff_response = flatten_updated_records(spend_diff_response)
      
    return earliest_points_sorted, updated_records, spend_diff_response, points_to_spend 

#In [129]: 
def flatten_updated_records(updated_records: list[dict]): 
    flat_updated_records = [] 
    all_payers = set([x["payer"] for x in updated_records]) 
    for payer in all_payers: # get all points per payer and 
        sum_payer_records = [x for x in updated_records if x["payer"] == payer] 
        sum_pts = sum([x["points"] for x in sum_payer_records]) 
        flat_updated_records.append({"payer": payer, "points": sum_pts})  
        
    return flat_updated_records

payer_points = [
    { "payer": "DANNON", "points": 1000, "timestamp": "2020-11-02T14:00:00Z" },
    { "payer": "UNILEVER", "points": 200, "timestamp": "2020-10-31T11:00:00Z" },
    { "payer": "DANNON", "points": -200, "timestamp": "2020-10-31T15:00:00Z" },
    { "payer": "MILLER COORS", "points": 10000, "timestamp": "2020-11-01T14:00:00Z" },
    { "payer": "DANNON", "points": 300, "timestamp": "2020-10-31T10:00:00Z" },            
]

points = 5000

earliest_points_sorted, updated_records, spend_diff_response, points_to_spend = spend_points(payer_points, points)

print(
    "ORIGINAL DATA + UPDATES: ", 
    json.dumps(earliest_points_sorted, indent=4, sort_keys=True),
    "",
    "UPDATED PAYER RECORDS: ",
    json.dumps(updated_records, indent=4, sort_keys=True),
    "",
    "SPEND DIFF PAYER RECORDS: ",
    json.dumps(spend_diff_response, indent=4, sort_keys=True),
    "",
    "REMAINING POINTS: ",
    points_to_spend,
    "",
sep="\n")