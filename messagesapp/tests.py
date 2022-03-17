from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(post="This is a Post.")
    


    def test_post_created(self):

        post = Post.objects.get(id=1)
        
        self.assertEqual(post.post, "This is a Post.")




    def test_posts_page_url_correct(self):

        response = self.client.get("/messagesapp/posts/")

        self.assertEqual(response.status_code, 200)


    
    # def test_posts_page_url_by_name(self):

    #     response = self.client.get(reverse("posts"))

    #     self.assertEqual(response.status_code, 200)
    


    def test_posts_page_template_verification(self):

        response = self.client.get("/messagesapp/posts/")

        self.assertTemplateUsed(response, "messagesapp/home.html")