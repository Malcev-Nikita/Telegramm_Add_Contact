from telethon.sync import TelegramClient
from telethon import functions, types
from random import randrange
from time import sleep

from config import NAME, API_ID, API_HASH


f = open("base.txt")
fd = f.read()
parse = fd.split('\n')

i = 0
a = 300
limit = 500

with TelegramClient(NAME, API_ID, API_HASH) as client:

    while (a < limit):

        while (i < 50):

            result = client(functions.contacts.ImportContactsRequest(
                contacts=[types.InputPhoneContact(
                    client_id = randrange(-2**63, 2**63),
                    phone = parse[a + i],
                    first_name = f'Base {a + i}',
                    last_name = ''
                )]
            ))

            i += 1
            print(f'{a + i}: Base {a + i} - {parse[a + i]}')

        i = 0
        a += 50
        sleep(320)