# Generated by Django 4.0.6 on 2022-08-06 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_volunteeritem_participate_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteeritem',
            name='participate_items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pi', to='content.participateitems'),
        ),
    ]
