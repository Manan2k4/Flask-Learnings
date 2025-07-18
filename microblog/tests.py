
import os
os.environ['DATABASE_URL'] = 'sqlite://'

from datetime import datetime, timedelta, timezone
import unittest
from app import create_app, db
from app.models import User, Post

class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        u = User()
        u.username = 'susan'
        u.email = 'susan@example.com'
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_avatar(self):
        u = User()
        u.email = 'john@example.com'
        self.assertEqual(u.avatar(128), 
                        'https://www.gravatar.com/avatar/d4c74594d841139328695756648b6bd6?d=identicon&s=128')

    def test_follow(self):
        u1 = User()
        u1.username = 'john'
        u1.email = 'john@example.com'
        
        u2 = User()
        u2.username = 'susan'
        u2.email = 'susan@example.com'
        
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        
        self.assertEqual(u1.following.count(), 0)
        self.assertEqual(u2.followers.count(), 0)
        
        u1.follow(u2)
        db.session.commit()
        
        self.assertTrue(u1.is_following(u2))
        self.assertEqual(u1.following.count(), 1)
        self.assertEqual(u2.followers.count(), 1)
        
        u1.unfollow(u2)
        db.session.commit()
        
        self.assertFalse(u1.is_following(u2))
        self.assertEqual(u1.following.count(), 0)
        self.assertEqual(u2.followers.count(), 0)

    def test_follow_posts(self):
        # Create users
        u1 = User()
        u1.username = 'john'
        u1.email = 'john@example.com'
        
        u2 = User()
        u2.username = 'susan'
        u2.email = 'susan@example.com'
        
        u3 = User()
        u3.username = 'mary'
        u3.email = 'mary@example.com'
        
        u4 = User()
        u4.username = 'david'
        u4.email = 'david@example.com'
        
        db.session.add_all([u1, u2, u3, u4])

        # Create posts
        now = datetime.now(timezone.utc)
        p1 = Post(body="post from john", author=u1,
                 timestamp=now + timedelta(seconds=1))
        p2 = Post(body="post from susan", author=u2,
                 timestamp=now + timedelta(seconds=4))
        p3 = Post(body="post from mary", author=u3,
                 timestamp=now + timedelta(seconds=3))
        p4 = Post(body="post from david", author=u4,
                 timestamp=now + timedelta(seconds=2))
        
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()

        # Setup followers
        u1.follow(u2)
        u1.follow(u4)
        u2.follow(u3)
        u3.follow(u4)
        db.session.commit()

        # Check following posts
        f1 = u1.following_posts().all()
        f2 = u2.following_posts().all()
        f3 = u3.following_posts().all()
        f4 = u4.following_posts().all()
        
        self.assertEqual(f1, [p2, p4, p1])
        self.assertEqual(f2, [p2, p3])
        self.assertEqual(f3, [p3, p4])
        self.assertEqual(f4, [p4])

if __name__ == '__main__':
    unittest.main(verbosity=2)