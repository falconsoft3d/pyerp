# coding: utf-8
u"""
Wrapper que permite generar un objeto ``Client`` con el que se pueden efectuar
consultas a la API de pagos (payment) de Flow. Ejemplos de uso::

    # Genera un nuevo cliente, con las credenciales y en modo Sandbox
    cliente = Client('CLIENT-API-KEY', 'CLIENT-SECRET-KEY', True)

    # realizar un pago
    res = cliente.payment.create(
        'SO001', 'Pago de productos', 5000, 'juanito@mail.com',
        'http://localhost:8069/payment/flow/confirmation',
        'http://localhost:8069/payment/flow/return')
    url_redireccion = '{url}?token={token}'.format(**res.json())

    # Consultar estado de un pago mediante el token generado
    res = cliente.payment.get_token('PAYMENT-TOKEN')
    print res.json().get('status')

    # Consultar estado de un pago mediante el order generado por el comercio
    res = cliente.payment.get_order('SALE-ORDER-1')
    print res.json().get('status')
"""
# Standard Library
import hashlib
import hmac

# Thirdparty Library
import requests


class Payment(object):
    u""" Genera un objeto Payment, usado por el cliente para hacer consultas
    relacionadas con pagos (generar pago, consultar estados de los mismos) """

    _endpoint = '/payment'

    def __init__(self, client):
        self.client = client

    def create(self, reference, subject, amount, email, url_confirmation,
               url_return, currency='CLP', gateway='9'):
        u""" Crea un pago usando los parámetros indicados, devuelve la respuesta
        de tipo requests.Response, donde se obtendrá la URL y el token,
        necesarios para generar la redirección a la página de pago de Flow. """

        data = {
            'apiKey': self.client._api_key,
            'commerceOrder': reference,
            'subject': subject,
            'currency': currency,
            'amount': amount,
            'email': email,
            'paymentMethod': gateway,
            'urlConfirmation': url_confirmation,
            'urlReturn': url_return
        }
        return self.client.post(self._endpoint + '/create', data)

    def get_token(self, token):
        u""" Consulta el estado de un pago usando el token generado por Flow """
        data = {
            'apiKey': self.client._api_key,
            'token': token
        }
        return self.client.get(self._endpoint + '/getStatus', data)

    def get_order(self, order):
        u""" Consulta el estado de un pago usando la orden generada por el
        comercio """
        data = {
            'apiKey': self.client._api_key,
            'commerceId': order
        }
        return self.client.get(self._endpoint + '/getStatusByCommerceId', data)


class Client(object):
    u""" Genera un objeto Client listo para hacer consultas a la API de Flow """

    _url_prod = 'https://www.flow.cl/api'
    _url_sandbox = 'https://flow.tuxpan.com/api'

    def __init__(self, api_key, secret_key, sandbox=False):
        self._api_key = api_key
        self._secret_key = secret_key
        self._sandbox = sandbox
        self._payment = Payment(self)

    @property
    def payment(self):
        u""" Permite acceder a la API de pagos directamente desde el cliente """
        return self._payment

    @property
    def url(self):
        u""" Devuelve la URL a consultar según el entorno configurado """
        return self._url_sandbox if self._sandbox else self._url_prod

    def get(self, endpoint, data):
        data.update({'s': self.sign_data(data)})
        return requests.get(self.url + endpoint, params=data)

    def post(self, endpoint, data):
        u""" Realiza una petición de tipo POST al `endpoing` indicado, enviando
        la `data` y generando su respectiva firma """
        data.update({'s': self.sign_data(data)})
        return requests.post(self.url + endpoint, data=data)

    def sign_data(self, data):
        u""" Devuelve la firma cifrada con la data que se enviará a Flow """
        sorted_data = sorted(data.items(), key=lambda x: x[0])
        string = '&'.join('%s=%s' % (key, val) for key, val in sorted_data)
        return hmac.new(self._secret_key, str(string.encode('utf-8')), hashlib.sha256).hexdigest()
