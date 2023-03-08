# Generated by Django 3.2 on 2023-03-07 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20230306_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavouritesList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favourites', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.favourite')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]