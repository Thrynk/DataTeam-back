#from django.test import TestCase
#import math
#import requests

## Create your tests here.

#content = requests.get('http://192.168.43.51/api2/tennisPlayer/?orderby=name&name__iexact=NaDal')
#data  =content.json()
#print(data)
#print(data['results'])

#url='http://192.168.43.51/api2/tennisPlayer/{id}'.format(id=str(1))
#content = requests.get(url)
#data = content.json()
#print(data)
#print(data['id'])

#url='http://192.168.43.51/api2/tennisPlayer/{id}/match/'.format(id='4742')#str(obj.winner.id))
#content = requests.get(url)
#data = content.json()
#print(data)
#print(data['results'])

##x=30
##page_nombre=10
##y=x/page_nombre

##print(math.ceil(y))

##L=[1,5,7,8]
###L.remove(16)

##print(L[0:100])

##parms_possibles=[
##            'exact',
##            'iexact',
##            'contains',
##            'icontains',
##            'in',
##            'gt',
##            'gte',
##            'lt',
##            'lte',
##            'startswith',
##            'istartswith',
##            'endswith',
##            'iendswith',
##            'range',
##            'date',
##            'year',
##            'iso_year',
##            'month',
##            'day',
##            'week',
##            'week_day',
##            'quarter',
##            'time',
##            'hour',
##            'minute',
##            'second',
##            'isnull',
##            'regex',
##            'iregex',
##            ]

a=[1,2,3]

def plusdeux(a):
    b=a
    b.remove(2)
    return b


b = plusdeux(a)

print(a)