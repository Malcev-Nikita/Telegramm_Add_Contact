from telethon.sync import TelegramClient
from telethon import functions, types
from random import randrange

from config import NAME, API_ID, API_HASH


f = open("base.txt")
fd = f.read()
parse = fd.split('\n')


with TelegramClient(NAME, API_ID, API_HASH) as client:

    i = 0
    a = 100

    while (i < 50):

        result = client(functions.contacts.ImportContactsRequest(
            contacts=[types.InputPhoneContact(
                client_id = randrange(-2**63, 2**63),
                phone = parse[i],
                first_name = f'Base {a + i}',
                last_name = ''
            )]
        ))

        i += 1
        print(f'Base {i}')