"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('private/', include('private.urls')),
    path('user/', include('users.urls')),
    path('digitalObject/', include('digitalObjects.urls')),
    path('suggestion/', include('suggestions.urls')),
    path('contacts/', include('contacts.urls')),
    path('news/', include('news.urls')),
    path('virtualReality/', include('virtualReality.urls')),
    path('histories/', include('histories.urls')),
    path('products/', include('products.urls')),
    path('sales/', include('sales.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)