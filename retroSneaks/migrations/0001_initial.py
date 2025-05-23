# Generated by Django 5.2 on 2025-05-01 11:12

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessoryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CustomizationOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('condition', models.CharField(choices=[('new', 'Brand New'), ('like_new', 'Like New'), ('used', 'Used - Good'), ('worn', 'Used - Worn')], max_length=20)),
                ('size', models.CharField(choices=[('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45')], max_length=3)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('stock', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('tag_type', models.CharField(choices=[('new_arrival', 'New Arrival'), ('hot_sale', 'Hot Sale')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('stock', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='retroSneaks.accessorycategory')),
            ],
        ),
        migrations.CreateModel(
            name='AccessoryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='accessory_images/')),
                ('accessory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='retroSneaks.accessory')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('accessory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='retroSneaks.accessory')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='retroSneaks.cart')),
                ('customizations', models.ManyToManyField(blank=True, to='retroSneaks.customizationoption')),
                ('shoe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='retroSneaks.shoe')),
            ],
        ),
        migrations.CreateModel(
            name='CustomizationPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customization_type', models.CharField(choices=[('base_color', 'Base Color'), ('accent_color', 'Accent Color'), ('sole_color', 'Sole Color'), ('lace_color', 'Lace Color'), ('pattern', 'Pattern')], max_length=20)),
                ('color', models.CharField(blank=True, choices=[('black', 'Black'), ('white', 'White'), ('red', 'Red'), ('blue', 'Blue'), ('green', 'Green'), ('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('gray', 'Gray'), ('multi', 'Multi-color')], max_length=20, null=True)),
                ('pattern', models.CharField(blank=True, choices=[('solid', 'Solid'), ('striped', 'Striped'), ('polka', 'Polka Dot'), ('camo', 'Camouflage'), ('geometric', 'Geometric'), ('gradient', 'Gradient')], max_length=20, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'unique_together': {('customization_type', 'color', 'pattern')},
            },
        ),
        migrations.AddField(
            model_name='customizationoption',
            name='customization_price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='retroSneaks.customizationprice'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('shipping_address', models.TextField()),
                ('payment_method', models.CharField(max_length=50)),
                ('items', models.ManyToManyField(to='retroSneaks.cartitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='customizationoption',
            name='shoe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customization_options', to='retroSneaks.shoe'),
        ),
        migrations.CreateModel(
            name='ShoeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='shoe_images/')),
                ('is_primary', models.BooleanField(default=False)),
                ('shoe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='retroSneaks.shoe')),
            ],
        ),
        migrations.AddField(
            model_name='shoe',
            name='tags',
            field=models.ManyToManyField(blank=True, to='retroSneaks.tag'),
        ),
    ]
