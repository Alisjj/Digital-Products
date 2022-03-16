from django.db import models
from users.models import User
import dateutil.relativedelta as relativedelta
# Create your models here.

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interval = models.CharField(max_length=120)
    started = models.DateTimeField()
    active = models.BooleanField(default=False)
    plan_id = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if self.interval == "Monthly":
            self.active = True
            if self.started == self.started + relativedelta(months=1):
                self.active = False

        if self.interval == "Yearly":
            self.active = True
            if self.started == self.started + relativedelta(years=1):
                self.active = False

        if self.interval == "Cancelled":
            self.active = False

        if self.started == "Cancelled":
            self.active = False

        if self.plan_id == "Cancelled":
            self.active = False

            
        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return "Membership for" + self.user.username + self.active

    

