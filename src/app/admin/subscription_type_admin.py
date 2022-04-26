from sqladmin import ModelAdmin

from ..models import SubscriptionType


class SubscriptionTypeAdmin(ModelAdmin, model=SubscriptionType):
    name = "Subscription"
    name_plural = "Subscriptions"
    icon = "fa-solid fa-dollar-sign"
    column_list = [SubscriptionType.id, SubscriptionType.type]
    form_columns = [SubscriptionType.type]
    can_export = False
    can_view_details = False
    page_size = 25
    page_size_options = [10, 25, 50, 100]