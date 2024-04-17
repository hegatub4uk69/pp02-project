from django.db import models


class Masters(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    work_experience = models.IntegerField()


class Machines(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    year_of_release = models.IntegerField()


class Details(models.Model):
    name = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    sizes = models.CharField(max_length=255)


class Orders(models.Model):
    order_date = models.DateField()
    client = models.CharField(max_length=255)
    quantity = models.IntegerField()


class PartsManufacturing(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    detail = models.ForeignKey(Details, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machines, on_delete=models.CASCADE)
    master = models.ForeignKey(Masters, on_delete=models.CASCADE)
    date_end = models.DateField()
    quantity = models.IntegerField()
