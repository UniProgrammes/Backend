from django.db import models

class Course(models.Model):
    courseid = models.AutoField(primary_key=True)
    coursename = models.CharField(max_length=255)
    coursecode = models.CharField(max_length=255)
    credits = models.DecimalField(max_digits=5, decimal_places=2)
    educationallevel = models.CharField(max_length=255)
    coursedescription = models.TextField()
    mainarea = models.CharField(max_length=255)

    class Meta:
        db_table = 'dev"."course'
        managed = False
