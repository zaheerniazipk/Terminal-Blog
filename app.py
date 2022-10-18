import pprint
from database import Database
from models.post import Post

# Database Interaction
Database.initialize()

# Verify all post methods

# post = Post(blog_id='123', title="Another great post", content="This is some sample content", author="Zaheer")
# post.save_to_mongo()

# post = Post.from_mongo('b0cb7d3411e44a0d927ea9e04fdfe92c')
# pprint.pprint(post)

posts = Post.from_blog('123')
for post in posts:
    pprint.pprint(post)