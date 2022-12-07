from django.test import TestCase
from django.contrib.auth.models import User
from web.models import Post, Category


class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')

        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')
        testuser1.save()

        test_post = Post.objects.create(
            category_id=1, title='Post Title', discount='1', content='Post Content', price='10', validity='2022-10-02',slug='post-title', author_id=1, status='published')
        test_post.save()

    def test_web_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        discount = f'{post.discount}'
        content = f'{post.content}'
        title = f'{post.title}'
        price = f'{post.price}'
        validity = f'{post.validity}'
        status = f'{post.status}'
        self.assertEqual(author, 'test_user1')
        self.assertEqual(title, 'Post Title')
        self.assertEqual(discount, '1.0')
        self.assertEqual(price, '10')
        self.assertEqual(content, 'Post Content')
        self.assertEqual(validity, '2022-10-02')
        self.assertEqual(str(post), "Post Title")
        self.assertEqual(status, 'published')
        self.assertEqual(str(cat), "django")