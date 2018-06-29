# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remov` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from mreg.validators import validate_mac_address, validate_ttl
from django.core.exceptions import ValidationError


class Zones(models.Model):
    zoneid = models.AutoField(primary_key=True)
    name = models.TextField(unique=True)
    primary_ns = models.TextField()
    email = models.EmailField(blank=True, null=True)
    serialno = models.BigIntegerField(blank=True, null=True)
    refresh = models.IntegerField(blank=True, null=True)
    retry = models.IntegerField(blank=True, null=True)
    expire = models.IntegerField(blank=True, null=True)
    ttl = models.IntegerField(blank=True, null=True, validators=[validate_ttl])

    class Meta:
        db_table = 'zones'

    def clean(self):
        # Make sure refresh, retry, and expire values adhere to database constraints
        check_refresh = self.refresh > self.retry
        check_expire = self.expire > self.refresh + self.retry
        check_retry = self.retry >= 300

        if not check_refresh:
            raise ValidationError('Refresh may not be less than or equal to retry.')
        if not check_expire:
            raise ValidationError('Expire must be greater than retry + refresh ({}).'.format(self.refresh+self.retry))
        if not check_retry:
            raise ValidationError('Retry may not be less than 300.')


class Ns(models.Model):
    nsid = models.AutoField(primary_key=True)
    zoneid = models.ForeignKey('Zones', models.DO_NOTHING, db_column='zoneid')
    name = models.TextField()
    ttl = models.IntegerField(blank=True, null=True, validators=[validate_ttl])

    class Meta:
        db_table = 'ns'


class HinfoPresets(models.Model):
    hinfoid = models.AutoField(primary_key=True)
    cpu = models.TextField()
    os = models.TextField()

    class Meta:
        db_table = 'hinfo_presets'


class Hosts(models.Model):
    hostid = models.AutoField(primary_key=True)
    name = models.TextField(unique=True)
    contact = models.EmailField()
    ttl = models.IntegerField(blank=True, null=True, validators=[validate_ttl])
    hinfo = models.ForeignKey(HinfoPresets, models.DO_NOTHING, db_column='hinfo', blank=True, null=True)
    loc = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'hosts'


class Ipaddress(models.Model):
    hostid = models.ForeignKey(Hosts, models.DO_NOTHING, db_column='hostid')
    ipaddress = models.GenericIPAddressField(unique=True)
    macaddress = models.TextField(blank=True, null=True, validators=[validate_mac_address])

    class Meta:
        db_table = 'ipaddress'


class PtrOverride(models.Model):
    hostid = models.ForeignKey(Hosts, models.DO_NOTHING, db_column='hostid')
    ipaddress = models.GenericIPAddressField(unique=True)

    class Meta:
        db_table = 'ptr_override'


class Txt(models.Model):
    txtid = models.AutoField(primary_key=True)
    hostid = models.ForeignKey(Hosts, models.DO_NOTHING, db_column='hostid')
    txt = models.TextField()

    class Meta:
        db_table = 'txt'


class Cname(models.Model):
    hostid = models.ForeignKey('Hosts', models.DO_NOTHING, db_column='hostid')
    cname = models.TextField()
    ttl = models.IntegerField(blank=True, null=True, validators=[validate_ttl])

    class Meta:
        db_table = 'cname'


class Subnets(models.Model):
    subnetid = models.AutoField(primary_key=True)
    range = models.TextField()  # This field type is a guess.
    description = models.TextField(blank=True, null=True)
    vlan = models.IntegerField(blank=True, null=True)
    dns_delegated = models.NullBooleanField()

    class Meta:
        db_table = 'subnets'


class Naptr(models.Model):
    naptrid = models.AutoField(primary_key=True)
    preference = models.IntegerField(blank=True, null=True)
    orderv = models.IntegerField(blank=True, null=True)
    flag = models.CharField(max_length=1, blank=True, null=True)
    service = models.TextField()
    regex = models.TextField(blank=True, null=True)
    replacement = models.TextField()

    class Meta:
        db_table = 'naptr'


class Srv(models.Model):
    srvid = models.AutoField(primary_key=True)
    service = models.TextField()
    priority = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    ttl = models.IntegerField(blank=True, null=True, validators=[validate_ttl])
    target = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'srv'
