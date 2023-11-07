from datetime import datetime
from flask import request
from backend.models.engine.db_storage import db
from backend.models.blog import Blog
from backend.api.v1.views import app_views


def format_blog(blog):
    return {
        "id": blog.id,
        "author": blog.author_name,
        "content": blog.text,
        "created_at": blog.created_at,
    }


# Create blog
@app_views.route("/blogs", methods=["POST"], strict_slashes=False)
def create_blog():
    try:
        name = request.json["author_name"]
        content = request.json["text"]
        blog = Blog(name, content)
        db.session.add(blog)
        db.session.commit()
        return format_blog(blog)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return "An error occured", 500


# Get all blogs
@app_views.route("/blogs", methods=["GET"], strict_slashes=False)
def get_blogs():
    blogs = Blog.query.order_by(id.asc()).all()
    blog_list = []
    for blog in blogs:
        blog_list.append(format_blog(blog))
    return {"blogs": blog_list}


# Get a single blog
@app_views.route("/blogs/<id>", methods=["GET"], strict_slashes=False)
def get_blog(id):
    blog = Blog.query.filter_by(id=id)
    formatted_blog = format_blog(blog)
    return {"blog": formatted_blog}


# Delete a blog
@app_views.route("/blogs/<id>", methods=["DELETE"], strict_slashes=False)
def delete_blog(id):
    blog = Blog.query.filter_by(id=id).one()
    db.session.delete(blog)
    db.session.commit()
    return f"Blog {Blog.id} deleted!"


# Edit a blog
@app_views.route("/blogs/<id>", methods=["PUT"], strict_slashes=False)
def edit_blog(id):
    blog = Blog.query.filter_by(id=id)
    name = request.json["author_name"]
    content = request.json["text"]
    blog = Blog(name, content)
    blog.update(dict(name=name, content=content, updated_at=datetime.utcnow))
    return {"blog": format_blog(blog).one()}
