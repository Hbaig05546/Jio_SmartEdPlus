from django.db import models
from accounts.models import Student


class Reward(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class RewardRedemption(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
    date_redeemed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} redeemed {self.reward.name} on {self.date_redeemed}"


class RewardRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
    date_requested = models.DateTimeField(auto_now_add=True)
    date_approved = models.DateTimeField(null=True, blank=True)
    date_rejected = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.user.username} requested {self.reward.name}"

    def is_approved(self):
        return self.date_approved is not None
    
    is_approved.boolean = True
    is_approved.short_description = "Approved?"