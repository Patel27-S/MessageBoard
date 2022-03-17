from django.urls import path

from messagesapp.views import HomePageView

app_name = 'messagesapp'

urlpatterns = [
    path("posts/", HomePageView.as_view(), name="posts")
]