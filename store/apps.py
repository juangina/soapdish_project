from django.apps import AppConfig


class StoreConfig(AppConfig):
    #default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'

    #Some files need to be "connected to the app for it to be activated by django"
    def ready(self):
        import store.signals
