from django.db import models


class Groups(models.Model):
    group_name = models.CharField(max_length=120, null=True)
    teacher_name = models.CharField(max_length=120, null=True)
    grade = models.SmallIntegerField(null=True)

    def __str__(self):
        return f"{self.group_name}_{self.teacher_name} ({self.grade})"

