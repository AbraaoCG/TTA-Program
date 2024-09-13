from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'


class MyAppConfig(AppConfig):
    name = 'my_app'

    def ready(self):
        import my_app.signals