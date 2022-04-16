from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from .forms import BlogForm
from .forms import CommentForm
from .models import Blog
from .models import Comment


# Create your views here.

def index(request):
    template = 'list.html'
    blogs = Blog.objects.all()
    context = {
         'blogs': blogs,
    }
    return render(request, template, context)

def add_blog(request):
	template = "add_blog.html"

	if request.method == "POST":
		form = BlogForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse_lazy('blog:index'))
	else:
		context = {
			'blog_form': BlogForm(),
		}
		return render(request, template, context)

def update_blog(request, blog_id):
	template = "update_blog.html"
	blog = Blog.objects.get(id=int(blog_id))

	if request.method == "POST":
		form = BlogForm(request.POST, instance=blog)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse_lazy('blog:index'))
	else:
		context = {
			'blog_form': BlogForm(instance=blog),
		}
		return render(request, template, context)	

def view_blog(request, blog_id):
	template = "view_blog.html"
	post = Blog.objects.get(id=int(blog_id))
	comments = post.comments.filter(active=True)
	new_comment = None

	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post = post
			new_comment.save()
			comment_form = CommentForm()
	else:
		comment_form = CommentForm()

	return render(request, template, {'post': post,
										'comments': comments,
										'new_comment': new_comment,
										'comment_form': comment_form})

"""	
	context = {
	    'blog': blog,
	}
	return render(request, template, context)	"""	
"""
def delete_comment(request, comment_id):
	comment = Comment.objects.get(id=int(comment_id))
	comment.delete()
	return HttpResponseRedirect("/")	 """

def delete_comment(request, comment_id):
	comment = Comment.objects.get(id=int(comment_id))
	comment.delete()
	return HttpResponseRedirect("/")

def delete_blog(request, blog_id):
	post = Blog.objects.get(id=int(blog_id))
	post.delete()
	return HttpResponseRedirect(reverse_lazy('blog:index'))


def login(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse_lazy('blog:index'))
	else:
		return HttpResponseRedirect(reverse_lazy('auth_login'))
