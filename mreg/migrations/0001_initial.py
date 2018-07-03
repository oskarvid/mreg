# Generated by Django 2.0.6 on 2018-07-02 12:31

from django.db import migrations, models
import django.db.models.deletion
import mreg.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.TextField()),
                ('ttl', models.IntegerField(blank=True, null=True, validators=[mreg.validators.validate_ttl])),
            ],
            options={
                'db_table': 'cname',
            },
        ),
        migrations.CreateModel(
            name='HinfoPresets',
            fields=[
                ('hinfoid', models.AutoField(primary_key=True, serialize=False)),
                ('cpu', models.TextField()),
                ('os', models.TextField()),
            ],
            options={
                'db_table': 'hinfo_presets',
            },
        ),
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('hostid', models.AutoField(primary_key=True, serialize=True)),
                ('name', models.TextField(unique=True)),
                ('contact', models.EmailField(max_length=254)),
                ('ttl', models.IntegerField(blank=True, null=True, validators=[mreg.validators.validate_ttl])),
                ('loc', models.TextField(blank=True, null=True, validators=[mreg.validators.validate_loc])),
                ('comment', models.TextField(blank=True, null=True)),
                ('hinfo', models.ForeignKey(blank=True, db_column='hinfo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mreg.HinfoPresets')),
            ],
            options={
                'db_table': 'hosts',
            },
        ),
        migrations.CreateModel(
            name='Ipaddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddress', models.GenericIPAddressField(unique=True)),
                ('macaddress', models.TextField(blank=True, null=True, validators=[mreg.validators.validate_mac_address])),
                ('hostid', models.ForeignKey(db_column='hostid', on_delete=django.db.models.deletion.DO_NOTHING, to='mreg.Hosts')),
            ],
            options={
                'db_table': 'ipaddress',
            },
        ),
        migrations.CreateModel(
            name='Naptr',
            fields=[
                ('naptrid', models.AutoField(primary_key=True, serialize=False)),
                ('preference', models.IntegerField(blank=True, null=True)),
                ('orderv', models.IntegerField(blank=True, null=True)),
                ('flag', models.CharField(blank=True, max_length=1, null=True, validators=[mreg.validators.validate_naptr_flag])),
                ('service', models.TextField()),
                ('regex', models.TextField(blank=True, null=True)),
                ('replacement', models.TextField()),
                ('hostid', models.ForeignKey(db_column='hostid', on_delete=django.db.models.deletion.DO_NOTHING, to='mreg.Hosts')),
            ],
            options={
                'db_table': 'naptr',
            },
        ),
        migrations.CreateModel(
            name='Ns',
            fields=[
                ('nsid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('ttl', models.IntegerField(blank=True, null=True, validators=[mreg.validators.validate_ttl])),
            ],
            options={
                'db_table': 'ns',
            },
        ),
        migrations.CreateModel(
            name='PtrOverride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddress', models.GenericIPAddressField(unique=True)),
                ('hostid', models.ForeignKey(db_column='hostid', on_delete=django.db.models.deletion.DO_NOTHING, to='mreg.Hosts')),
            ],
            options={
                'db_table': 'ptr_override',
            },
        ),
        migrations.CreateModel(
            name='Srv',
            fields=[
                ('srvid', models.AutoField(primary_key=True, serialize=False)),
                ('service', models.TextField(validators=[mreg.validators.validate_srv_service_text])),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('port', models.IntegerField(blank=True, null=True)),
                ('ttl', models.IntegerField(blank=True, null=True, validators=[mreg.validators.validate_ttl])),
                ('target', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'srv',
            },
        ),
        migrations.CreateModel(
            name='Subnets',
            fields=[
                ('subnetid', models.AutoField(primary_key=True, serialize=False)),
                ('range', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('vlan', models.IntegerField(blank=True, null=True)),
                ('dns_delegated', models.NullBooleanField()),
            ],
            options={
                'db_table': 'subnets',
            },
        ),
        migrations.CreateModel(
            name='Txt',
            fields=[
                ('txtid', models.AutoField(primary_key=True, serialize=False)),
                ('txt', models.TextField()),
                ('hostid', models.ForeignKey(db_column='hostid', on_delete=django.db.models.deletion.DO_NOTHING, to='mreg.Hosts')),
            ],
            options={
                'db_table': 'txt',
            },
        ),
        migrations.CreateModel(
            name='Zones',
            fields=[
                ('zoneid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(unique=True)),
                ('primary_ns', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('serialno', models.BigIntegerField(blank=True, null=True)),
                ('refresh', models.IntegerField(blank=True, null=True)),
                ('retry', models.IntegerField(blank=True, null=True)),
                ('expire', models.IntegerField(blank=True, null=True)),
                ('ttl', models.IntegerField(blank=True, null=True, validators=[mreg.validators.validate_ttl])),
            ],
            options={
                'db_table': 'zones',
            },
        ),
        migrations.AddField(
            model_name='ns',
            name='zoneid',
            field=models.ForeignKey(db_column='zoneid', on_delete=django.db.models.deletion.DO_NOTHING, to='mreg.Zones'),
        ),
        migrations.AddField(
            model_name='cname',
            name='hostid',
            field=models.ForeignKey(db_column='hostid', on_delete=django.db.models.deletion.DO_NOTHING, to='mreg.Hosts'),
        ),
    ]
