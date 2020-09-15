from django.urls import path, include

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-listing', CreateListing.as_view(), name='add_listing'),
    path('listings/<slug:slug>/', ListingView.as_view(), name='listing'),
    path('addInfo',addInfo,name='addInfo'),
    path('lists',lists,name='lists'),
    path('diss',dissatisfy, name='diss'),
    path('profile',profile, name='profile'),
]