import operator
from collections import defaultdict

points1 = [{"payer": "DANNON", "points": 1500, "timestamp": "2022-05-00:30Z"},
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

#code to sort list by payer and datestamp: It works!
# points1.sort(key = operator.itemgetter('payer','timestamp'))
# print ("result", str(points1))


#To render_available_points
def render_available_points(request):   
    pass


#store ordered dictionary in variable

#create new dict with 'payer': '[list of points]'
