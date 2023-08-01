from django.apps import AppConfig


class AutenticacionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "autenticacion"

# myapp/apps.py

    def ready(self):
        import autenticacion.signals  # Importa tus señales aquí