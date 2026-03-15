from django.db import models


class Salary(models.Model):

    amount = models.FloatField()

    def __str__(self):
        return str(self.amount)


class Expense(models.Model):

    title = models.CharField(max_length=200)
    amount = models.FloatField()
    category = models.CharField(max_length=100, default="Other")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title