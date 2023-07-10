from django.db import models
from django.utils import timezone

class Coupon(models.Model):
    code = models.CharField(max_length=8, unique=True)
    usage_count = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    expiry_date = models.DateTimeField(null=True, blank=True)
    discount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.code

    def use_coupon(self):
        if self.usage_count > 0:
            self.usage_count -= 1
            if self.usage_count == 0:
                self.is_available = False
            self.save()

    def is_expired(self):
        if self.expiry_date is None:
            return False
        return self.expiry_date < timezone.now()
