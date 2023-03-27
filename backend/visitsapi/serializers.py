from rest_framework.serializers import ModelSerializer

from .models import SiteVisit


class SiteVisitSerializer(ModelSerializer):
    class Meta:
        model = SiteVisit
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}
