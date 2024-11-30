from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('review/', views.review, name='review'),  # Form page
    path('submit-review/', views.submit_review, name='submit_review'),  # Submission handler
]

