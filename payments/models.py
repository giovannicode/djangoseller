from django.db import models


class Payment(models.Model):
    total = models.DecimalField(max_digits=14, decimal_places=2)

    def __unicode__(self):
        return str(self.total)
