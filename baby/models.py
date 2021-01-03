import uuid

from django.db import models


class BabyManager(models.Manager):

    def default(self):
        try:
            return self.get_queryset().order_by('-id')[0]
        except IndexError:
            new_baby = Baby()
            new_baby.save()
            return new_baby


class Baby(models.Model):
    born = models.BooleanField(default=False)
    name = models.CharField(max_length=30, blank=True)
    due_date = models.DateField(null=True, blank=True, default=None)
    born_on = models.DateTimeField(null=True, blank=True, default=None)
    secret_id = models.UUIDField(default=uuid.uuid4)

    objects = BabyManager()

    def get_absolute_url(self):
        from django.shortcuts import reverse
        return reverse('secret', args=[self.secret_id])

    def __str__(self):
        return f'{self.name} ({self.id})'

    class Meta:
        verbose_name_plural = 'Babies'
