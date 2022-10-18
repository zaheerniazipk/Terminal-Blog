import pprint
from database import Database
from models.blog import Blog

# Database Interaction
Database.initialize()

blog = Blog(author="Zaheer",
            title="Sample Title",
            description="Sample Description")

# Verify all Blog methods
blog.new_post()
blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)
pprint.pprint(blog.get_posts())