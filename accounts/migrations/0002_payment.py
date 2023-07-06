# Generated by Django 4.0.5 on 2023-07-06 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('amount', models.PositiveIntegerField()),
                ('verified', models.BooleanField(default=False)),
                ('ref', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]