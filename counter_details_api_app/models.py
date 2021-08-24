from django.db import models


class CounterDetails(models.Model):
    counter_id = models.CharField(max_length=30, blank=True, null=True)
    kpi_name = models.CharField(primary_key=True, max_length=50)
    interval = models.FloatField(blank=True, null=True)
    counter_condition = models.CharField(max_length=70, blank=True, null=True)
    kpi_type = models.CharField(max_length=20, blank=True, null=True)
    table_name = models.CharField(max_length=50, blank=True, null=True)
    msc_col_name = models.CharField(max_length=50, blank=True, null=True)
    time_col_name = models.CharField(max_length=50, blank=True, null=True)
    kpi_val_col_name = models.CharField(max_length=50, blank=True, null=True)
    db = models.ForeignKey("DbDetails", models.DO_NOTHING, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "counter_details"


class DbDetails(models.Model):
    db_id = models.FloatField(primary_key=True)
    db_name = models.CharField(max_length=30)
    db_port = models.FloatField(blank=True, null=True)
    db_service_name = models.CharField(max_length=30, blank=True, null=True)
    db_user = models.CharField(max_length=20, blank=True, null=True)
    db_password = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "db_details"
        unique_together = (("db_id", "db_name"),)
