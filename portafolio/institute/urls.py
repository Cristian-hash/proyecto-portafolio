from django.urls import path
from django.urls.conf import include

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import handler403
from .views import main_views, auth_views, user_views, course_views, inscription_views

urlpatterns = [
    path('', main_views.index, name='index'),

    path('login', auth_views.login, name='login'),
    path('register', auth_views.register, name='register'),
    path('logout', auth_views.logout, name='logout'),

    path('add_user', user_views.UserCreateView.as_view(), name='add_user'),
    path('view_users', user_views.UserListView.as_view(), name='view_users'),
    path('edit_user/<int:pk>', user_views.UserUpdateView.as_view(), name='edit_user'),
    path('delete_user/<int:pk>',user_views.UserDeleteView.as_view(), name='delete_user'),

    path('add_course', course_views.CourseCreateView.as_view(), name='add_course'),
    path('view_courses', course_views.CourseListView.as_view(), name='view_courses'),
    path('edit_course/<int:pk>', course_views.CourseUpdateView.as_view(), name='edit_course'),
    path('delete_course/<int:pk>', course_views.CourseDeleteView.as_view(), name='delete_course'),

    path('add_inscription', inscription_views.add_inscription, name='add_inscription'),
    path('view_inscriptions', inscription_views.view_inscriptions, name='view_inscriptions'),
    path('edit_inscription/<int:id_Inscription>', inscription_views.edit_inscription, name='edit_inscription'),
    path('delete_inscription/<int:id_Inscription>', inscription_views.delete_inscription, name='delete_inscription'),
    path('captcha/', include('captcha.urls')),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
