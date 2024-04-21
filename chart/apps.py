from django.apps import AppConfig


class ChartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chart'
    verbose_name = 'Статистика'

    def ready(self):
        import chart.signals
