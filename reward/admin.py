from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Reward)
admin.site.register(RewardRedemption)
admin.site.register(RewardRequest)