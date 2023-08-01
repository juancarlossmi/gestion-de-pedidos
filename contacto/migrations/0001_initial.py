# Generated by Django 4.2.3 on 2023-07-31 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contacto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50)),
                ("apellido", models.CharField(max_length=50)),
                ("correo", models.EmailField(max_length=50)),
                ("telefono", models.IntegerField(blank=True, null=True)),
            ],
            options={"verbose_name": "Contacto", "verbose_name_plural": "Contactos",},
        ),
    ]