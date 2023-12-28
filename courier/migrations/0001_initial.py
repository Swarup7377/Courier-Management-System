# Generated by Django 3.1.1 on 2022-04-20 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BranchName', models.CharField(max_length=250, null=True)),
                ('BranchContactnumber', models.CharField(max_length=12, null=True)),
                ('BranchEmail', models.CharField(max_length=50, null=True)),
                ('BranchAddress', models.CharField(max_length=200, null=True)),
                ('BranchCity', models.CharField(max_length=150, null=True)),
                ('BranchState', models.CharField(max_length=150, null=True)),
                ('BranchPincode', models.CharField(max_length=6, null=True)),
                ('BranchCountry', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RefNumber', models.CharField(max_length=100, null=True)),
                ('SenderName', models.CharField(max_length=250, null=True)),
                ('SenderContactnumber', models.CharField(max_length=12, null=True)),
                ('SenderAddress', models.CharField(max_length=250, null=True)),
                ('SenderCity', models.CharField(max_length=150, null=True)),
                ('SenderState', models.CharField(max_length=150, null=True)),
                ('SenderPincode', models.CharField(max_length=6, null=True)),
                ('SenderCountry', models.CharField(max_length=250, null=True)),
                ('RecipientName', models.CharField(max_length=250, null=True)),
                ('RecipientContactnumber', models.CharField(max_length=12, null=True)),
                ('RecipientAddress', models.CharField(max_length=250, null=True)),
                ('RecipientCity', models.CharField(max_length=150, null=True)),
                ('RecipientState', models.CharField(max_length=150, null=True)),
                ('RecipientPincode', models.CharField(max_length=6, null=True)),
                ('RecipientCountry', models.CharField(max_length=150, null=True)),
                ('CourierDes', models.CharField(max_length=250, null=True)),
                ('ParcelWeight', models.CharField(max_length=150, null=True)),
                ('ParcelDimensionlen', models.CharField(max_length=150, null=True)),
                ('ParcelDimensionwidth', models.CharField(max_length=150, null=True)),
                ('ParcelDimensionheight', models.CharField(max_length=150, null=True)),
                ('ParcelPrice', models.CharField(max_length=150, null=True)),
                ('Status', models.CharField(max_length=100, null=True)),
                ('CourierDate', models.DateTimeField(auto_now_add=True)),
                ('SenderBranch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courier.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StaffMobilenumber', models.CharField(max_length=12, null=True)),
                ('status', models.CharField(max_length=150, null=True)),
                ('StaffRegdate', models.DateTimeField(auto_now_add=True)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courier.branch')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CourierTracking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark', models.CharField(max_length=150, null=True)),
                ('status', models.CharField(max_length=150, null=True)),
                ('StatusDate', models.DateField(null=True)),
                ('CourierId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courier.courier')),
            ],
        ),
    ]