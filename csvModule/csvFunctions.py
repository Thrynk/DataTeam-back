import os
import csv
from api.models import *
from django.conf import settings

def csv_to_model(csvFile,model):
    BASE_DIR = settings.BASE_DIR
    path = os.path.join(BASE_DIR, 'csvModule\\{cvsFileName}'.format(cvsFileName=csvFile))
    nameFields=[field.name for field in model._meta.fields]
    nameFields.remove('id')
    with open(path) as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            dico={}
            i=0
            for name in nameFields:
                dico[name]=row[i]
                i=+1
            test = model.objects.create(**dico)