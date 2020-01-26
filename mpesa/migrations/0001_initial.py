# Generated by Django 3.0.2 on 2020-01-26 14:24

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
            name='C2BPayments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TransactionType', models.CharField(blank=True, max_length=50, null=True)),
                ('TransID', models.CharField(blank=True, max_length=30, null=True)),
                ('TransTime', models.CharField(blank=True, max_length=50, null=True)),
                ('TransAmount', models.CharField(blank=True, max_length=120, null=True)),
                ('BusinessShortCode', models.CharField(blank=True, max_length=50, null=True)),
                ('BillRefNumber', models.CharField(blank=True, max_length=120, null=True)),
                ('InvoiceNumber', models.CharField(blank=True, max_length=120, null=True)),
                ('OrgAccountBalance', models.CharField(blank=True, max_length=120, null=True)),
                ('ThirdPartyTransID', models.CharField(blank=True, max_length=120, null=True)),
                ('MSISDN', models.CharField(blank=True, max_length=25, null=True)),
                ('FirstName', models.CharField(blank=True, max_length=50, null=True)),
                ('MiddleName', models.CharField(blank=True, max_length=50, null=True)),
                ('LastName', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LNMOnline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_request_id', models.CharField(max_length=50)),
                ('checkout_request_id', models.CharField(max_length=120)),
                ('result_code', models.IntegerField()),
                ('result_desc', models.TextField()),
                ('amount', models.FloatField()),
                ('mpesa_receipt_number', models.CharField(max_length=15)),
                ('balance', models.CharField(blank=True, max_length=12, null=True)),
                ('transaction_date', models.DateTimeField()),
                ('phonenumber', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='profile.jpg', upload_to='profile_pictures/')),
                ('email', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profile',
                'ordering': ('username',),
            },
        ),
    ]
