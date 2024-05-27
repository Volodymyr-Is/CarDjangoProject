"""
URL configuration for game_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.contrib import admin
from game_store import settings
from django.conf.urls.static import static
from django.urls import path
from game_store_app.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', allGamesMain, name='home'),
    path('shop/', allGamesShop, name='shop'),
    path('games/<int:gameId>', gameById, name='gameById'),
    path('games/<str:data>', gamesByData, name='gamesByData'),
    path('games/', searchGame, name='searchGame'),
    path('shop/<str:data>', filteredShop, name='filteredShop'),
    path('purchase/<int:gameId>', purchaseGame, name='purchaseGame'),
    path('games/<int:gameId>/comment/add/', addComment, name='addComment'),
    path('games/<int:gameId>/comment/<int:commentId>/edit/', editComment, name='editComment'),
    path('games/<int:gameId>/comment/<int:commentId>/delete/', deleteComment, name='deleteComment'),

    path('accounts/login/', login_view, name='login'),
    path('accounts/register/', register_view, name='register'),
    path('accounts/logout/', logout_view, name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
