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
    born_on = models.DateTimeField(null=True, blank=True, default=None)

    objects = BabyManager()

    def __repr__(self):
        return f'{self.name} ({self.id})'

    class Meta:
        verbose_name_plural = 'Babies'
