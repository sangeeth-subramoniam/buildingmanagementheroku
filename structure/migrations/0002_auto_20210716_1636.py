# Generated by Django 3.2.5 on 2021-07-16 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storemaster',
            old_name='ReadingAreaNo',
            new_name='ReadingArea',
        ),
        migrations.AlterField(
            model_name='metermaster',
            name='StoreNO',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storemaster', to='structure.storemaster'),
        ),
        migrations.AlterUniqueTogether(
            name='storemaster',
            unique_together={('StoreNO', 'ReadingArea')},
        ),
    ]
