# Blueprint
from database import Database


class Post(object):
    # Constructor
    def __init__(self, blog_id, title, content, author, date, id):
        # Dynamic class Attributes | Properties
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = id

    # Method
    def save_to_mongo(self):
        Database.insert(collection='posts', data=self.json())

    # Method
    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'created_date': self.created_date
        }