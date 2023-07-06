# Generated by Django 4.0.5 on 2023-07-06 02:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15, null=True)),
                ('norsical', models.CharField(max_length=200, null=True)),
                ('patrol', models.CharField(choices=[('Adaka MP', 'Adaka MP'), ('Aso MP', 'Aso MP'), ('Baglina MP', 'Baglina MP')], max_length=200)),
                ('designation', models.CharField(choices=[('Skull', 'Skull'), ('BOT', 'BOT'), ('Dechand', 'Deckhand')], max_length=200)),
                ('Do_You_Use_Hard_Drugs', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], max_length=200)),
                ('passport', models.ImageField(default='avatar.svg', null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]