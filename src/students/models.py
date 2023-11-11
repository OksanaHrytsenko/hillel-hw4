from random import random, randint

from django.db import models
from faker import Faker


class Students(models.Model):
    first_name = models.CharField(max_length=120, null=True)
    last_name = models.CharField(max_length=120, null=True)
    email = models.EmailField(null=True)
    grade = models.SmallIntegerField(null=True, default=100)

    def __str__(self):
        return f"{self.first_name}_{self.last_name} {self.email}({self.grade})"

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        for _ in range(0 < count <= 100):
            cls.objects.create(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                grade=random.randint(1, 100)
            )

