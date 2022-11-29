# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


account_sid = 'ACa2d60cd5f68c50b32c81a6682f869eb9'
auth_token = 'ef14618f109463f2fb9e14edc0896070'

client = Client(account_sid, auth_token)
client.messages.create(from_='+16402027908',
                       to='+917977292053',
                       body='Hey Soham, You are Genius.Billionaire.Philanthropist.')

