from app.models import Blog,User, BlogCom
from app import db
import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'chemistry')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)
    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('chemistry'))


def setUp(self):
        self.user_lugaga = User(username = 'lugaga',password = 'password', email = 'maureezgaga@gmail.com', bio = 'i am a software engineer', profile_pic_path ='./static/photos/engineer.png' )
        self.new_blog = Blog(blog_id=12345,blog='blog'user = self.user_lugaga )
        self.new_blogcom = BlogCom(blog_id=12345,blog='blogcom'user = self.user_lugaga )

def tearDown(self):
        Blog.query.delete()
        User.query.delete

def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.blog_id,12345)
        self.assertEquals(self.new_blog.blog,'enter anything')


def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all())>0)

def test_get_blog_by_id(self):

        self.new_blog.save_blog()
        get_blog = Blog.get_blog(12345)
        self.assertTrue(len(got_blogs) == 1)
