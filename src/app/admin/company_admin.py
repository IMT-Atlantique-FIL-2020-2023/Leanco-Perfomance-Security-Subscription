from sqladmin import ModelAdmin

from ..models import Company


class CompanyAdmin(ModelAdmin, model=Company):
    name = "Company"
    name_plural = "Companies"
    icon = "fa-solid fa-building"
    column_list = [Company.id, Company.name]
    form_columns = [Company.name]
    can_view_details = False
    page_size = 25
    page_size_options = [10, 25, 50, 100]
