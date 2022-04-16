from django.conf.urls import url
from . import views
from .views import index, add_blog, update_blog, view_blog, delete_comment, login, delete_blog 


urlpatterns = [
    url(r'^$', login, name='login'),
    url(r'^index$', index, name='index'),
    url(r'^add_blog$', add_blog, name='add-blog'),
    url(r'^update_blog/(?P<blog_id>\d+)$', update_blog, name='update-blog'),
    url(r'^view_blog/(?P<blog_id>\d+)$', view_blog, name='view-blog'),
    url(r'^delete_comment/(?P<comment_id>\d+)$', delete_comment, name='delete-comment'),
    url(r'^delete_blog/(?P<blog_id>\d+)$', delete_blog, name='delete-blog'),

]
