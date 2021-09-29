from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name = "Madushan", 
                        email = "madushannipuna1997@gmail.com",
                        is_staff = True,
                        is_superuser = True,
                        phone = "0718895181",
                        gender = "Male"
        )

        user.set_password("Madushan@13")
        user.save()

    dependencies = [
        
    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
    