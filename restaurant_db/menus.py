import csv

path = 'restaurant_db/static/csv/'
restaurants = []
csm = {}
avg_csm_vs_yelp_factor = {}
v_factor_vs_average_tip = {}
v_factor_vs_yelp_factor = {}
dates ={}
dlist = []
with open( path + 'csm.csv', 'rb') as f :
    reader = csv.reader(f, delimiter=',')
    for row in reader : 

        if row[1] in csm.keys() :
            csm[row[1]][row[0]] = row[2]
        else :
            csm[row[1]] = {}
            csm[row[1]][row[0]] = row[2]

with open( path + 'avg_csm_vs_yelp_factor.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader :
        avg_csm_vs_yelp_factor[row[0]] = {}
        avg_csm_vs_yelp_factor[row[0]]['yelp'] = row[2]
        avg_csm_vs_yelp_factor[row[0]]['csm']  = row[1]

with open( path + 'v_factor_vs_average_tip.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    for r in reader :
        v_factor_vs_average_tip[r[0]] = {}
        v_factor_vs_average_tip[r[0]]['v'] = r[1]
        v_factor_vs_average_tip[r[0]]['tip']=r[2]

with open( path + 'v_factor_vs_yelp_factor.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    for r in reader:
        v_factor_vs_yelp_factor[r[0]] = {}
        v_factor_vs_yelp_factor[r[0]]['v'] = r[1]
        v_factor_vs_yelp_factor[r[0]]['yelp']=r[2]

for i in v_factor_vs_average_tip.keys() :
    restaurants.append(i)

for i in range(1,31) :
    if i < 10 :
        dates['November ' + str(i)] = '2014-11-0' + str(i)
    else :
        dates['November ' + str(i)] = '2014-11-' + str(i)
    dlist.append('November ' + str(i))
restaurants.sort()

class Data() :
    restaurants = restaurants
    csm = csm
    csm_yelp = avg_csm_vs_yelp_factor
    v_tip = v_factor_vs_average_tip
    v_yelp= v_factor_vs_yelp_factor
    dates = dates
    dlist = dlist
