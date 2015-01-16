from django.conf.urls import patterns, url

from views import HomeView, APIView, JqueryView, JhtmlView, AddUserView, SampleView, ValidationView, UserView, UserListView, EditView, DeleteView

urlpatterns = patterns("app",
    url(r'^$',HomeView.as_view(),name='home'),
    url(r'^get-list/$',APIView.as_view(),name='get_list'),
    url(r'^jquery/$',JqueryView.as_view(),name='jquery'),
    url(r'^jhtml/$',JhtmlView.as_view(),name='jhtml'),
    url(r'^add-car/$',AddUserView.as_view(),name='add-car'),
    url(r'^sample/$',SampleView.as_view(),name='sample'),
    url(r'^jvalid/$',ValidationView.as_view(),name='jvalid'),
    url(r'^add-user/$',UserView.as_view(),name='add-user'),
    url(r'^all-user/$',UserListView.as_view(),name='all-user'),
    url(r'^edit-user/$',EditView.as_view(),name='edit-user'),
    url(r'^delete-user/$',DeleteView.as_view(),name='delete-user'),    
    )