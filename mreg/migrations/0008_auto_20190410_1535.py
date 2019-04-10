# Generated by Django 2.2 on 2019-04-10 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mreg', '0007_hostgroup_hostgroupmember'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hostgroup',
            options={'ordering': ('name',)},
        ),
        migrations.RenameField(
            model_name='hostgroup',
            old_name='hostgroup_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='hostgroupmember',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='hostmembers', to='mreg.HostGroup'),
        ),
        migrations.AlterField(
            model_name='hostgroupmember',
            name='host',
            field=models.ForeignKey(db_column='host', on_delete=django.db.models.deletion.PROTECT, related_name='hostgroups', to='mreg.Host'),
        ),
        migrations.AlterModelTable(
            name='hostgroupmember',
            table='hostmember',
        ),
    ]
