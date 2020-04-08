# Django Library
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

PAYPAL_MODE = (
    ("sandbox", "Sandbox"),
    ('online', 'Online')
)

class PaypalConfig(models.Model):
    mode = models.CharField(_("Mode"), choices=PAYPAL_MODE, max_length=64, default='sandbox')
    paypal_client_id = models.CharField(_("Paypal Client Id"), max_length=250)
    paypal_client_secret = models.CharField(_("Paypal Client Secret"), max_length=250)

    online = models.BooleanField('Online', default=False)


    def get_absolute_url(self):
        return reverse('paypal:paypal-config', kwargs={'pk': self.pk})

    def dload_data(self):
        self.load_data = True
