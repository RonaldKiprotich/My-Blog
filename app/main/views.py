from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from . import main
from .. import db
from ..models import User,Blog
from .forms import BlogForm


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/blog/new_blog',methods= ['GET','POST'])
@login_required
def new_blog():
    blogForm = BlogForm()
    if blogForm.validate_on_submit():
        titleBlog=blogForm.blogTitle.data
        description = blogForm.blogDescription.data
        newBlog = Blog(title_blog=titleBlog, description=description, user= current_user)
        newBlog.saveBlog()
        return redirect(url_for('main.allBlogs'))
    title = 'New Blog'
    return render_template('new_blogs.html', title=title, blog_form=blogForm)