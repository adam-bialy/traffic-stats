from django.core.exceptions import FieldError
from django.db.models import Count
from django.db.models import Q
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SiteVisit
from .serializers import SiteVisitSerializer


class SiteVisitListCreateView(ListCreateAPIView):
    serializer_class = SiteVisitSerializer
    queryset = SiteVisit.objects.order_by("id")


class SiteVisitGroupView(APIView):
    def get(self, request, *args, **kwargs):
        # Parse the query parameter which indicates the field to group by
        group_by_field = request.query_params.get("group")
        if group_by_field is None:
            return Response(
                "Required: field to group by (`group` query parameter).",
                status=status.HTTP_400_BAD_REQUEST,
            )
        if group_by_field == "interaction_type":
            return Response(
                "Cannot group by this field only.",
                status=status.HTTP_400_BAD_REQUEST,
            )
        # Perform GROUP BY  and COUNT query with this field
        try:
            queryset = self.get_aggregated_data(group_by_field)
        except FieldError:
            return Response(
                f"Cannot group site visits by `{group_by_field}` - this field does not exist.",
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(queryset)

    @staticmethod
    def get_aggregated_data(group_by_field):
        queryset = (
            SiteVisit.objects.values(group_by_field)
            .annotate(
                view=Count(
                    "interaction_type", filter=Q(interaction_type=SiteVisit.VIEW)
                ),
                read=Count(
                    "interaction_type", filter=Q(interaction_type=SiteVisit.READ)
                ),
                open=Count(
                    "interaction_type", filter=Q(interaction_type=SiteVisit.OPEN)
                ),
            )
            .order_by(group_by_field)
        )
        return queryset
