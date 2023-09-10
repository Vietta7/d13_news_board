from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *


app_name = 'desk'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('desk/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('desk/create/', PostCreateView.as_view(), name='post_create'),
    path('desk/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('desk/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('desk/<int:pk>/reply/', reply, name='reply'),
    path('desk/<int:pk>/replied/', replied, name='replied'),
    path('private/', PrivateOfficeView.as_view(), name='private_office'),
    path('private/<int:pk>/', ReplyDetailView.as_view(), name='reply_detail'),
    path('private/<int:pk>/delete/', ReplyDeleteView.as_view(), name='reply_delete'),
    path('private/<int:pk>/approve/', reply_approve, name='reply_approve'),
    path('private/by_post/<int:post_id>/', SortedByPostView.as_view(), name='sorted_by_post'),
    path('subscribe/', subscribe, name='subscribe'),
    path('unsubscribe/', unsubscribe, name='unsubscribe'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout_user, name='logout'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)