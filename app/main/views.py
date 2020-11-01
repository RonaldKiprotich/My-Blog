from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from . import main
from .. import db
from ..models import User,Blog
from .forms import BlogForm


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/blog/newBlog',methods = ['GET','POST'])
@login_required
def newBlog():
    blogForm = BlogForm()
    if blogForm.validate_on_submit():
        titleBlog=blogForm.blogTitle.data
        description = blogForm.blogDescription.data
        newBlog = Blog(title_blog=titleBlog, description=description, user= current_user)
        newBlog.save_blog()
        return redirect(url_for('main.allBlogs'))
    title = 'New Blog'
    return render_template('new_blogs.html', title=title, blog_form=blogForm)
@main.route('/blog/allblogs', methods=['GET', 'POST'])
@login_required
def allBlogs():
    blogs = Blog.get_all_blogs()
    return render_template('blogs.html', blogs=blogs)