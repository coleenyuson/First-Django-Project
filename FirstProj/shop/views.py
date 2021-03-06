from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = "shop/index.html"

class VehicleView(generic.ListView):
    template_name = 'shop/vehicle.html'
    context_object_name = 'all_vehicle'

    def get_queryset(self):
        return Vehicle.objects.all()

class ProfileView(generic.TemplateView):
    template_name = "shop/profile.html"

class VehicleUpd(UpdateView):
    model = Vehicle
    fields = ['plate_no', 'make', 'model', 'engine_no', 'chasis_no', 'color', 'type','fkid_cust']

class VehicleAdd(CreateView):
    model = Vehicle
    fields = ['plate_no', 'make', 'model', 'engine_no', 'chasis_no', 'color', 'type','fkid_cust']

class CustomerView(generic.ListView):
    template_name = 'shop/customer.html'
    context_object_name = 'all_cust'

    def get_queryset(self):
        return Customer.objects.all()

class CustomerAdd(CreateView):
    model = Customer
    fields = ['cust_name', 'address', 'tel_no', 'allow_ar', 'bad_acc']

class CustomerDelete(DeleteView):
    model = Customer
    success_url = reverse_lazy('shop:customer')

class CustomerUpd(UpdateView):
    model = Customer
    fields = ['cust_name', 'address', 'tel_no', 'allow_ar', 'bad_acc']

class TechnicianView(generic.ListView):
    template_name = 'shop/technician.html'
    context_object_name = 'all_tech'

    def get_queryset(self):
        return Technician.objects.all()

class TechnicianAdd(CreateView):
    model = Technician
    fields = ['last_name', 'first_name', 'mid_name', 'gender', 'birth_date', 'address', 'spec_area']

class SupplierView(generic.ListView):
    template_name = 'shop/supplier.html'
    context_object_name = 'all_supplier'

    def get_queryset(self):
        return Supplier.objects.all()

class SupplierAdd(CreateView):
    model = Supplier
    fields = ['supplier_name', 'address', 'tel_no']

class JobsView(generic.ListView):
    template_name = 'shop/jobs.html'
    context_object_name = 'all_jobs'

    def get_queryset(self):
        return Job.objects.all()

class JobsAdd(CreateView):
    model = Job
    fields = ['job_desc', 'service_fee', 'fkid_jobType', 'service_time', 'service_uom']

class PartsView(generic.ListView):
    template_name = 'shop/parts.html'
    context_object_name = 'all_parts'

    def get_queryset(self):
        return Parts.objects.all()

class PartsAdd(CreateView):
    model = Parts
    fields = ['part_no', 'part_desc', 'srp', 'latest_rr', 'latest_rr_date', 'latest_supplier', 'uom']

