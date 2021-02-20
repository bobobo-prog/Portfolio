from datetime import datetime, timezone
from django.db import models

class Count(models.Model):
    id = models.AutoField(primary_key=True)
    host = models.TextField()
    vis_day = models.IntegerField(default=0)
    vis_month = models.IntegerField(default = 0)

    def __str__(self):
        return(self.host[:50] + " " + str(self.vis_month))



