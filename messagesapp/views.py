from msilib.schema import ListView
from pdb import post_mortem
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.


class HomePageView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "messagesapp/home.html"
    
