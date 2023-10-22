from django.db import models


class Logs(models.Model):
    id = models.CharField(max_length=50)
    create_date = models.DateTimeField()
    log = models.TextField(max_length=300)
    cluster = models.CharField(verbose_name='Кластер')
    cluster_name = models.CharField(verbose_name='Название Кластера')

    def __str__(self):
        return self.id
