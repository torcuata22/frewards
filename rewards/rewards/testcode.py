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
    



# ordered_points = (sorted(points1, key = operator.itemgetter('payer', 'timestamp')))
# # ordered={}
# # keys = ['payer', 'points']
# # points2 = {key:value for key, value in ordered.items() if key in keys}
# # print (points2)

# # But this one works -->create dictionary form two lists: 
# for i in range(0,10):
#      x = ordered_points[i]['timestamp']
#      print (x)
 
# # #delete timestamp key from dictionary
# del_key = 'timestamp'    
# for items in ordered_points:
#     if del_key in items:
#         del items[del_key]
#     print (ordered_points)




def spend_points(payer_points_dict: list[dict], points_to_spend: int): 
    ''' 
    Spends points in points_to_spend in pay_points_dict['points'], with points spent in earliest 
    transactions first ACCEPTS: payer_points_dict: list of dictionaries w/ schema [payer:str, points:int, 
    timestamp: date/timestamp] points_to_spend: points to spend (int)  
    RETURNS: earliest_points_sorted: original list of dicts w/ edits updated_records: updated records, 
    flattened (payer, points) spend_diff_response: points differential, intended as a returned response (payer, points) 
    points_to_spend: remaining points 
    '''

# sort data structure by timestamp, earliest records first   
updated_records, spend_diff_response = [], []  # spend points across earliest payers, modify dict in-place 
earliest_points_sorted = sorted(points1, key=lambda d: d["timestamp"])  
#I added this:
points_to_spend = 5000
      
while points_to_spend > 0: 
    for record in earliest_points_sorted:   
        curr_points = record['points'] # reverse sign for existing negative balances  

    if curr_points < points_to_spend: 
        record['points'] = 0 
        points_to_spend += (-1 * curr_points) 
    else: 
        record['points'] -= points_to_spend 
        points_to_spend = 0  # track updated records & records for response 
        updated_records.append({"payer": record["payer"], "points": record['points']}) 
        spend_diff_response.append({"payer": record["payer"], "points": record['points'] - curr_points})  # if all payers eval'd, break the spend and return remaining points

        if record == earliest_points_sorted[-1]: 
            break  
    # updated_records = flatten_updated_records(updated_records) 
    # spend_diff_response = flatten_updated_records(spend_diff_response)  

        return earliest_points_sorted, updated_records, spend_diff_response, points_to_spend 

#In [129]: 
    def flatten_updated_records(updated_records: list[dict]): 
        ''' 
ACCEPTS:  updated_records: list of dictionaries with schema [payer:str, points:int]  
RETURNS: flat_updated_records: collapsed list of dicts with payer: summed points
    '''
    flat_updated_records = [] 
    all_payers = set([x["payer"] for x in updated_records]) 
    for payer in all_payers: # get all points per payer and 
        sum_payer_records = [x for x in updated_records if x["payer"] == payer] 
        sum_pts = sum([x["points"] for x in sum_payer_records]) 
        flat_updated_records.append({"payer": payer, "points": sum_pts})  
        
    return flat_updated_records 