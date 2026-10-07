from django.db import models


class FuelStation(models.Model):
    opis_truckstop_id = models.IntegerField(db_index=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=10)
    rack_id = models.IntegerField()
    retail_price = models.DecimalField(
        max_digits=8,
        decimal_places=4,
    )

    # The original CSV doesn't contain coordinates.
    # We will populate these during the data preparation phase.
    latitude = models.FloatField(
        null=True,
        blank=True,
    )
    longitude = models.FloatField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["state", "city", "name"]
        indexes = [
            models.Index(fields=["state", "city"]),
            models.Index(fields=["retail_price"]),
        ]

    def __str__(self):
        return f"{self.name} - {self.city}, {self.state}"