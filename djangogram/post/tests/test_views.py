from email.mime import image
from urllib import response
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile


class TestPosts(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username = 'test2', email = 'test2@test2.com', password = 'test2'
        )
    
    def test_get_posts_page(self):
        url = reverse('post:post_create')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/post_create.html')
    
    def test_creating_posts(self):
        login = self.client.login(username = 'test3', password = 'test3')
        self.assertTrue(login)
        
        url = reverse('post:post_create')
        image = SimpleUploadedFile('test.jpg', b'whatevercontents')
        response = self.client.post(
            url,
            { 'image': image, 'caption': 'test test' }
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/base.html')
        
    def test_post_posts_create_not_login(self):
        url = reverse('post:post_create')
        image = SimpleUploadedFile('test.jpg', b'whatevercontents')
        response = self.client.post(
            url,
            { 'image': image, 'caption': 'test test' }
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/main.html')