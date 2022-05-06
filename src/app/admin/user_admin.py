from sqladmin import ModelAdmin

from app.models import User


# Configuration page admin pour les utilisateurs
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
    column_details_list = [User.id,
                           User.firstname,
                           User.lastname,
                           User.email,
                           User.role,
                           User.subscription_startdate,
                           User.subscription_enddate,
                           User.company,
                           User.subscription_type]
