from sqladmin import ModelAdmin

from ..models import User


class UserAdmin(ModelAdmin, model=User):
    name = "User"
    name_plural = "Users"
    icon = "fa-solid fa-user"
    column_list = [User.id,
                   User.firstname,
                   User.lastname,
                   User.email,
                   User.role,
                   User.subscription_startdate,
                   User.subscription_enddate,
                   User.company,
                   User.subscription_type]

