# Generated by Django 3.2.10 on 2024-02-29 13:51

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_feedbacks_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbacks',
            name='imagem',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to='staticfiles_build/img/testimonial', variations={'thumb': {'crop': True, 'height': 180, 'width': 180}}, verbose_name='Imagem'),
        ),
    ]