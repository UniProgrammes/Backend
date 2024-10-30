from django.db import models

class Programme(models.Model):
    programmeid = models.AutoField(primary_key=True)
    programmename = models.CharField(max_length=255)
    degreetype = models.CharField(max_length=255)
    credits = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'dev"."programme'
        managed = False