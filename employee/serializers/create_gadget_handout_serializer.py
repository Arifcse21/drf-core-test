from rest_framework.serializers import ModelSerializer
from employee.models import GadgetHandout


class CreateGadgetHandoutSerializer(ModelSerializer):

    class Meta:
        model = GadgetHandout
        exclude = ("is_checked_out", "is_returned", "returned_at",)
