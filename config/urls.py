from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
   openapi.Info(
      title="py29 blog",
      default_version='v1',
      description="Test description",
      contact=openapi.Contact(email="contact@snippets.local"),

   ),
   public=True,

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('applications.account.urls')),
    path('api/movie/', include('applications.cinema.urls')),
    path('swagger/', schema_view.with_ui('swagger')),

]
