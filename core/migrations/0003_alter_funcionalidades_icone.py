# Generated by Django 5.0.1 on 2024-02-07 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_funcionalidades'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionalidades',
            name='icone',
            field=models.CharField(choices=[('lni-rocket', 'Foguete'), ('lni-laptop-phone', 'Eletrónicos'), ('lni-cog', 'Engrenagem'), ('lni-leaf', 'Folha'), ('lni-layers', 'Camadas')], max_length=16, verbose_name='Icone'),
        ),
    ]
