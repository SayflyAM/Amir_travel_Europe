from flask import Blueprint, render_template
from models import BlogPost

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/')
def list_posts():
    posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    return render_template('blog/list.html', posts=posts)


@blog_bp.route('/<slug>')
def detail(slug):
    post = BlogPost.query.filter_by(slug=slug).first_or_404()
    return render_template('blog/detail.html', post=post)
