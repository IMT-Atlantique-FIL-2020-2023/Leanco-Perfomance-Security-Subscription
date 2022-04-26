from sqladmin import ModelAdmin

from ..models import SubscriptionType


class SubscriptionTypeAdmin(ModelAdmin, model=SubscriptionType):
    column_list = [SubscriptionType.id, SubscriptionType.type]
