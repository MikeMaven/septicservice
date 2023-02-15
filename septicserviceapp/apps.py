from django.apps import AppConfig


class SepticserviceappConfig(AppConfig):
    name = 'septicserviceapp'
    verbose_name = 'Septic Info Service'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'septicserviceapp'
    house_canary_property_details_api = 'https://api.housecanary.com/v2/property/details'
