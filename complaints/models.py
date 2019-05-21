from django.db import models


class Complaint(models.Model):

    STATUS_CHOICES = (("CR", "Created"), ('PG', "Progress"), ('SD', "Solved"))

    order = models.OneToOneField("orders.Order", on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default="CR")
    text = models.TextField(blank=True)

    seller_text = models.TextField(blank=True)

    def __str__(self):
        return self.order.__str__()
