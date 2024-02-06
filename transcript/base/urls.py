
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('transcript/<int:student_id>/', views.transcript_view, name='transcript'),
    # Add other URL patterns as needed
]