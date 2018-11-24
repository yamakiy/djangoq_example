from django.db import models

class MyLog(models.Model):
    log_txt = models.CharField(max_length=255)
