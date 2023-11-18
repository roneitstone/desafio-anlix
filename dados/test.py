from django.utils import timezone

from datetime import datetime

epoch_value = 1637232000
dt_sao_paulo = timezone.make_aware(datetime.utcfromtimestamp(epoch_value), timezone=timezone.get_default_timezone())

print(dt_sao_paulo)
