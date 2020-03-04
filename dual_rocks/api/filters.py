import functools
import itertools
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q
from django_filters import FilterSet
from django_filters import rest_framework as filters


class MessageFilter(FilterSet):
    limit_messages_per_profile = filters.NumberFilter(
        label=_('limitar de mensagens por perfil'),
        method='filter_limit_messages_per_profile'
    )

    @classmethod
    def reduce_profile_tuples(cls, acc, t):
        a, b = t
        if (a, b) in acc or (b, a) in acc:
            return acc
        return acc + [(a, b)]

    def filter_limit_messages_per_profile(self, queryset, name, value):
        if not self.request.current_profile:
            return queryset

        profile_tuples = functools.reduce(
            MessageFilter.reduce_profile_tuples,
            queryset.values_list(
                'from_profile',
                'to_profile'
            ).distinct(),
            []
        )

        ids_list = list(
            itertools.chain.from_iterable(
                map(
                    lambda t: queryset.filter(
                        Q(from_profile_id=t[0], to_profile_id=t[1]) |
                        Q(from_profile_id=t[1], to_profile_id=t[0])
                    ).values_list('id', flat=True)[:value],
                    profile_tuples
                )
            )
        )

        return queryset.filter(id__in=ids_list)
