from django.db import models


class Logs(models.Model):

    log_id = models.CharField(max_length=50)
    create_date = models.DateTimeField()
    log = models.TextField(max_length=300)
    cluster = models.CharField(verbose_name='Кластер', max_length=10)
    cluster_name = models.CharField(verbose_name='Название Кластера', max_length=50)

    def __str__(self):
        return self.id


class User(models.Model):
    uuid = models.UUIDField()
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.email