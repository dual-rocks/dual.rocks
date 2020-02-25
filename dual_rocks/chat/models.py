from django.utils.translation import ugettext_lazy as _
from django.db import models
from dual_rocks.user_profile.models import Profile


class Message(models.Model):
    class Meta:
        ordering = ['-created_at']

    from_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='send_messages'
    )
    to_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='received_messages'
    )
    content = models.TextField(_('conteúdo'))
    created_at = models.DateTimeField(
        _('criado em'),
        auto_now=True,
        editable=False
    )

    def __str__(self):
        return f'Message #{self.id} / {self.from_profile} to {self.to_profile}'
