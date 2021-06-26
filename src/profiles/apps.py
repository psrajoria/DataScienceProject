from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'


#### Register and import your signal here and Go to __init__.py file to set it as default
    def ready(self):
        import profiles.signals
