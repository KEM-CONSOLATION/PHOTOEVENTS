# Generated by Django 3.2 on 2023-07-06 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile_which_is_your_preferred_meal_for_the_convaj_dinner_your_choice_will_be_indicated_on_your_mea'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Which_Is_Your_Preferred_Meal_For_the_Convaj_Dinner_Your_Choice_Will_Be_Indicated_on_Your_Meal_Ticket',
            new_name='Which_Is_Your_Preferred_Meal',
        ),
    ]
