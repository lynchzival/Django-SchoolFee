from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    course_desc = models.TextField()
    level = models.CharField(max_length=100)
    total_amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s" % (self.name, self.course_desc)


class Fee(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    fee_desc = models.TextField()
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
