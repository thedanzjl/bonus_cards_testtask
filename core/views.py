from rest_framework import viewsets

from .serializers import *
from .models import *


class CardsViewSet(viewsets.ModelViewSet):
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer

    def get_queryset(self):
        queryset = super(CardsViewSet, self).get_queryset()
        series = self.request.query_params.get('series', None)
        number = self.request.query_params.get('number', None)
        release_date = self.request.query_params.get('release_date', None)
        activity_end_date = self.request.query_params.get('activity_end_date', None)
        status = self.request.query_params.get('status', None)
        if series is not None:
            queryset = queryset.filter(series=series)
        if number is not None:
            queryset = queryset.filter(number=number)
        if release_date is not None:
            queryset = queryset.filter(release_date=release_date)
        if activity_end_date is not None:
            queryset = queryset.filter(activity_end_date=activity_end_date)
        if status is not None:
            queryset = queryset.filter(status=status)
        return queryset
