import csv
from api.models import *

TennisPlayer.objetc

def csv_to_bdd(path,modelClass):
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                return modelClass.objects.get(
                    name=row[1],
                    firtname=row[2],
                    )
            except modelClass.DoesNotExist:
                 return modelClass.objects.create(
                    name=row[1],
                    firtname=row[2],
                    nationality=row[5],
                    )