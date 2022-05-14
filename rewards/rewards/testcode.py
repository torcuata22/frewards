import operator
from collections import defaultdict
from itertools import groupby
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

#code to sort list by payer and datestamp:
#points2 = points1.sort(key = operator.itemgetter('payer','timestamp'))
#print ("result", str(points1))
# for i in range(0,10):  
#     x= points1[i]
#     test_list = list(x.values())
#     print(test_list)
    #y = x.fromkeys()
    #print(y)

    


# #to create a dictionary from another dictionary:
# ordered_points = (sorted(points1, key = operator.itemgetter('payer', 'timestamp'))) #list of dictionaries, so it won't create a new dict.
# ordered={}
# keys = ['payer', 'points']
# points2 = {key:value for key, value in ordered.items() if key in keys}
# print (points2)

# #But this one works -->create dictionary form two lists: 
# for i in range(0,10):
#     x = ordered_points[i]['timestamp']
#     print (x)
 
# #delete timestamp key from dictionary
# del_key = 'timestamp'    
# for items in ordered_points:
#     if del_key in items:
#         del items[del_key]
#     print (ordered_points)

# #substract points from payers (fixed amount):

# transaction = {"points": 500}

# for items in ordered_points:
#     if ordered_points[i]['points']:
#         pass
        #substract transaction['points'] from prdered_points[i]['points']????


