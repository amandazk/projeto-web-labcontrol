from django.conf.urls import url

from .views import (
    CaseList, CaseDestroy, CaseUpdate, CaseCreate, CaseGet, MachineList, ProblemList
)

urlpatterns = [
    url(r'work/$', CaseList.as_view()),
    url(r'work/(?P<pk>\d+)/$', CaseDestroy.as_view()),
    url(r'work/add/$', CaseCreate.as_view()),
    url(r'work/get/(?P<pk>\d+)/$', CaseGet.as_view()),
    url(r'work/edit/(?P<pk>\d+)/$', CaseUpdate.as_view()),
    url(r'work/machines/$', MachineList.as_view()),
    url(r'work/$', ProblemList.as_view())

]
