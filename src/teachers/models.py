from django.db import models


class Teachers(models.Model):
    first_name = models.CharField(max_length=120, null=True)
    last_name = models.CharField(max_length=120, null=True)
    email = models.EmailField(null=True)
    grade = models.SmallIntegerField(null=True)

    def __str__(self):
        return f"{self.first_name}_{self.last_name} {self.email}({self.grade})"
