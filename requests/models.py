from django.db import models

class Request(models.Model):
    id = models.IntegerField(name='ID', primary_key=True)
    createdby = models.IntegerField('CREATEDBY')
    custid = models.IntegerField('CUSTID')
    itemnum = models.CharField(name='ITEMNUM', max_length=40)
    description = models.CharField(name='DESCRIPTION', max_length=110)
    lead = models.IntegerField('LEAD')
    hours = models.IntegerField('HOURS')
    datedue = models.DateField('DATEDUE')
    cdate = models.DateField('CDATE')
    comment = models.CharField(name='COMMENT', max_length=255)
    ecr = models.BooleanField('ECR')
    ecrid = models.IntegerField('ECRID')
    new = models.BooleanField('NEW')
