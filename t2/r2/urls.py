from django.conf.urls import patterns, url
from r2 import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        url(r'^category/(?P<category_name>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
        url(r'^category/(?P<category_name_url>[\w\-]+)/$', views.category, name='category'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^search/$', views.search, name='search'),
        url(r'^f2/$', views.f2, name='f2'), # CJS playing wiht tabbed forms
        url(r'^goto/$', views.track_url, name='goto'),
        url(r'^like_category/$', views.like_category, name='like_category'),
        url(r'^suggest_category/$', views.suggest_category, name='suggest_category')
)
