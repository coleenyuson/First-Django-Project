from django.conf.urls import url
from . import views

app_name = 'shop'

urlpatterns = [

    # index/dashboard
    url(r'^$', views.IndexView.as_view(), name='index'),

    # profile
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),

    # vehicle management
    url(r'^vehicle-mgt/$', views.VehicleView.as_view(), name='vehicle'),

    # vehicle -add
    url(r'^vehicle-add/$', views.VehicleAdd.as_view(), name='vehicle-add'),

    # customer management
    url(r'^customer-mgt/$', views.CustomerView.as_view(), name='customer'),

    # customer -add
    url(r'^customer-add/$', views.CustomerAdd.as_view(), name='customer-add'),

    # customer -delete
    url(r'^customer-mgt/(?P<pk>[0-9]+)/del/$', views.CustomerDelete.as_view(), name='customer-del'),

    # customer -update
    url(r'^customer-mgt/(?P<pk>[0-9]+)/$', views.CustomerUpd.as_view(), name='customer-update'), #error

    # technician management
    url(r'^technician-mgt/$', views.TechnicianView.as_view(), name='technician'),

    # technician -add
    url(r'^technician-add/$', views.TechnicianAdd.as_view(), name='tech-add'),

    # Supplier management
    url(r'^supplier-mgt/$', views.SupplierView.as_view(), name='supplier'),

    # supplier -add
    url(r'^supploer-add/$', views.SupplierAdd.as_view(), name='supplier-add'),

    # Jobs management
    url(r'^jobs-mgt/$', views.JobsView.as_view(), name='jobs'),

    # Jobs -add
    url(r'^jobs-add/$', views.JobsAdd.as_view(), name='jobs-add'),

    # Parts management
    url(r'^parts-mgt/$', views.PartsView.as_view(), name='parts'),

    # Parts -add
    url(r'^parts-add/$', views.PartsAdd.as_view(), name='parts-add'),


]
