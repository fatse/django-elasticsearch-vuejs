from django.urls import path
from .views import AddStory, SearchStory, Articles, SearchStoryV2

urlpatterns = [
    path('api/stories/', AddStory.as_view(), name="add-story"),
    path('api/stories/search/', SearchStory.as_view(), name="search-story"),
    path('api/stories/searchV2/', SearchStoryV2.as_view(), name="search-story"),
    path('', Articles.as_view(), name="articles")
]
