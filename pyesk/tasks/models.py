from django.db import models
from django.utils.translation import ugettext_lazy as _


class Ticket(models.Model):
    PRIORITY_NAMES = (
        ('low', _('Low')),
        ('medium', _('Medium')),
        ('high', _('High')),
    )

    user = models.ForeignKey('auth.User')
    title = models.CharField(
        max_length=200,
        verbose_name=_('Title'),
    )
    code = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name=_('Ticket_ID'),
    )
    category = models.ForeignKey('Category')
    priority = models.CharField(
        max_length=40,
        choices=PRIORITY_NAMES,
        verbose_name=_('Priority'),
    )

    def save(self, *args, **kwargs):
        if not self.code:
            super().save(*args, **kwargs)
            self.code = '{}/{}'.format(self.category, self.pk)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Category'))

    def __str__(self):
        return self.name
