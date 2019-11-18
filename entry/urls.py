from django.conf.urls import url
from . import views

app_name = 'entry'

urlpatterns = [
    
    url(r'^create-stud-pd/$',views.stud_pd_entry,name="create_stud_pd"),
    url(r'^fee/(?P<usn>[\w]+)/$',views.update_stud_fee, name="update_stud_fee"),
]
