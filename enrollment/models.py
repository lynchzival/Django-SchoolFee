import decimal

from django.db import models

from course.models import Course
from student.models import Student


class Enroll(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    total_fee = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s - %s/%s $%s" % (self.student_id.name, self.course_id.name, self.course_id.level, self.total_fee)

    @property
    def paid(self):
        return sum([p.amount for p in self.payment_set.all()])

    def balance(self):
        return decimal.Decimal(self.total_fee) - self.paid

    def last_payment(self):
        return self.payment_set.order_by('-date_created').first()
