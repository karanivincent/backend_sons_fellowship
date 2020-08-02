from django.db import models

# Create your models here.


class Members(models.Model):
    name = models.CharField(max_length=250,)
    phone = models.CharField(max_length=13, null=True)
    visitor = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Campaign(models.Model):
    name = models.CharField(max_length=200)
    required_amount = models.PositiveIntegerField()
    contributed = models.PositiveIntegerField()
    description = models.TextField(null=True)
    start_date = models.DateField(auto_now_add=True, null=True)
    fullfill_date = models.DateField(null=True)
    active = models.BooleanField(default=True)


class Pledge(models.Model):
    pledger = models.ForeignKey(
        Members, related_name="pledges", on_delete=models.CASCADE)
    campaign = models.ForeignKey(
        Campaign, related_name="pledges", on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    contributed = models.IntegerField(default=0)
    settled = models.BooleanField(default=False)


class Attendance(models.Model):
    member = models.ForeignKey(
        Members, related_name="attendance", on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    seat_no = models.PositiveIntegerField(null=True)
