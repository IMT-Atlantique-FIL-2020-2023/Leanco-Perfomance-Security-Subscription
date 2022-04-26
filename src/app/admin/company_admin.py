from sqladmin import ModelAdmin

from ..models import Company


class CompanyAdmin(ModelAdmin, model=Company):
    column_list = [Company.id, Company.name]
