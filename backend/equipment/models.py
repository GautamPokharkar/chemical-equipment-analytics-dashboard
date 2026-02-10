from django.db import models

class EquipmentDataset(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    total_equipment = models.IntegerField()
    avg_flowrate = models.FloatField()
    avg_pressure = models.FloatField()
    avg_temperature = models.FloatField()
    type_distribution = models.TextField()
    
    def __str__(self):
        return f"Dataset @ {self.uploaded_at}"
