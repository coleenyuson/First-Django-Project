from django.db import models

class JobType(models.Model):
    remarks = models.CharField(max_length=100)

class Customer(models.Model):
    cust_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    tel_no = models.CharField(max_length=50)
    allow_ar = models.BooleanField(default=False)
    bad_acc = models.BooleanField(default=False)

class Vehicle(models.Model):
    plate_no = models.CharField(max_length=15)
    make = models.CharField(max_length=15)
    model = models.CharField(max_length=15)
    engine_no = models.CharField(max_length=50)
    chasis_no = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    type = models.CharField(max_length=15)
    fkid_cust = models.ForeignKey(Customer ,on_delete=models.CASCADE, default=0)

class Technician(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=20)
    mid_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=6)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=200)
    spec_area = models.CharField(max_length=15)

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    tel_no = models.CharField(max_length=50)

class Parts(models.Model):
    part_no = models.CharField(max_length=20)
    part_desc = models.CharField(max_length=50)
    srp = models.FloatField(default=0)
    latest_rr = models.CharField(max_length=45)
    latest_rr_date = models.DateField(null=True, blank=True)
    latest_supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, default=0)
    uom = models.CharField(max_length=5)

class Job(models.Model):
    job_desc = models.CharField(max_length=50)
    service_fee = models.FloatField(default=0)
    fkid_jobType = models.ForeignKey(JobType, on_delete=models.CASCADE, default=0)
    service_time = models.FloatField(default=0)
    service_uom = models.CharField(max_length=15)

class JobOrders(models.Model):
    job_date = models.DateTimeField(null=True, blank=True)
    target_date = models.DateTimeField(null=True, blank=True)
    stat = models.CharField(max_length=10)
    remarks = models.CharField(max_length=200)
    fkid_cust = models.ForeignKey(Customer, on_delete=models.CASCADE, default=0)
    fkplate_no = models.ForeignKey(Vehicle, on_delete=models.CASCADE, default=0)
    balance_acc = models.FloatField(default=0)
    dtlast_updated = models.DateTimeField(null=True, blank=True)
    id_user = models.IntegerField(default=0)

class JobOrderDetail(models.Model):
    fkid_jobOrder = models.ForeignKey(JobOrders, on_delete=models.CASCADE, default=0)
    fkid_job = models.ForeignKey(Job, on_delete=models.CASCADE, default=0)
    id_qty = models.FloatField(default=0)
    service_fee = models.FloatField(default=0)
    fkid_technician = models.ForeignKey(Technician, on_delete=models.CASCADE, default=0)

class JobPartUsage(models.Model):
    fkid_jobOrder = models.ForeignKey(JobOrders, on_delete=models.CASCADE, default=0)
    fkid_parts = models.ForeignKey(Parts, on_delete=models.CASCADE, default=0)
    qty = models.FloatField(default=0)
    srp = models.FloatField(default=0)
    unit_cost = models.FloatField(default=0)
    balance_qty = models.FloatField(default=0)
    balance_cost = models.FloatField(default=0)

class PartsOrder(models.Model):
    order_date = models.DateTimeField(null=True, blank=True)
    fkid_supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, default=0)
    status = models.CharField(max_length=12)
    processed = models.DateTimeField(null=True, blank=True)
    dtlast_updated = models.DateTimeField(null=True, blank=True)
    id_user = models.IntegerField(default=0)

class PartsOrderDetail(models.Model):
    fkid_parts = models.ForeignKey(Parts, on_delete=models.CASCADE, default=0)
    qty = models.FloatField(default=0)
    unit_cost = models.FloatField(default=0)
    balance_qty = models.FloatField(default=0)
    balance_cost = models.FloatField(default=0)

class PartsReceived(models.Model):
    receipt_dt = models.DateField(null=True, blank=True)
    fkid_supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, default=0)
    status = models.CharField(max_length=10)
    fkid_partsOrder = models.ForeignKey(PartsOrder, on_delete=models.CASCADE, default=0)
    processed = models.DateTimeField(null=True, blank=True)
    balance_acc = models.FloatField(default=0)

class PartsRecievedDetail(models.Model):
    id_parts = models.IntegerField(null=True)
    qty = models.FloatField(default=0)
    unit_cost = models.FloatField(default=0)
    balance_qty = models.FloatField(default=0)
    balance_cost = models.FloatField(default=0)
    dtlast_upd = models.DateTimeField(null=True, blank=True)
    id_user = models.IntegerField(default=0)
    fkidParts_received = models.ForeignKey(PartsReceived, on_delete=models.CASCADE, default=0)

class Collections(models.Model):
    collection_date = models.DateField(null=True, blank=True)
    fkid_cust = models.ForeignKey(Customer, on_delete=models.CASCADE, default=0)
    status = models.CharField(max_length=10)
    remarks = models.CharField(max_length=200)
    processed = models.DateTimeField(null=True, blank=True)
    balance_acc = models.FloatField(default=0)
    dtlast_upd = models.DateTimeField(null=True, blank=True)

class CollectionDetail(models.Model):
    fkid_collections = models.ForeignKey(Collections, on_delete=models.CASCADE, default=0)
    fkid_jobOrders = models.ForeignKey(JobOrders, on_delete=models.CASCADE, default=0)
    amount = models.FloatField(default=0)

class Payments(models.Model):
    payment_dt = models.DateField(null=True, blank=True)
    id_supplier = models.IntegerField(default=0)
    remarks = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    processed = models.DateTimeField(null=True, blank=True)
    balance_acc = models.FloatField(default=0)
    dtLast_upd = models.DateField(null=True, blank=True)
    id_user = models.IntegerField(default=0)

class PaymentsDetail(models.Model):
    fkid_payment = models.ForeignKey(Payments, on_delete=models.CASCADE, default=0)
    fkidParts_received = models.ForeignKey(PartsReceived, on_delete=models.CASCADE, default=0)
    amount = models.FloatField(default=0)
