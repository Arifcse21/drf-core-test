from rest_framework.serializers import ModelSerializer
from employee.models import GadgetHandout


class UpdateGadgetReturnSerializer(ModelSerializer):

    class Meta:
        model = GadgetHandout
        exclude = ("is_checked_out", "checked_out_at", "is_returned", "employer_id")

