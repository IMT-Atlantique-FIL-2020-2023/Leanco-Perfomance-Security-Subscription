from fastapi import FastAPI
from sqladmin import Admin
from starlette.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router
from app.core.config import settings
from app.db.session import engine
from app.models import User, Company, SubscriptionType
from app.admin.user_admin import UserAdmin
from app.admin.company_admin import CompanyAdmin
from app.admin.subscription_type_admin import SubscriptionTypeAdmin

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_BASE_URL}/openapi.json",

)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin) for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_BASE_URL)

admin = Admin(app, engine, title='LeanCo')
admin.register_model(UserAdmin)
admin.register_model(CompanyAdmin)
admin.register_model(SubscriptionTypeAdmin)

