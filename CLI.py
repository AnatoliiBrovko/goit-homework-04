import re

dict = {}
list_contacts = []

def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            print(f'IndexError: Give me name and phone please ')
        except KeyError:
            print(f'KeyError: Enter user name ')
        except ValueError:
            print(f"ValueError: This is not a phone number ")
    return inner


def hello():
    string = 'How can I help you?'
    return string


@input_error
def add_phone(message):
    message = message.strip().replace('add ', "")
    number = re.search(r'[+]?\d+', message)
    if not number:
        raise ValueError
    elif not message[:number.start() - 1]:
        raise KeyError
    else:
        dict = {'name': (message[:number.start() - 1].title()), 'phone': message[number.start():number.end()]}
        list_contacts.append(dict)
        string = 'Phone added'
        return string


@input_error
def change_phone(message):
    message = message.strip().replace('change ', "")
    number = re.search(r'[+]?\d+', message)
    if not number:
        raise ValueError
    elif not message[:number.start() - 1]:
        raise KeyError
    else:
        result = list(filter(lambda contact: (message[:number.start() - 1].title()) in contact['name'], list_contacts))
        result[0]['phone'] = message[number.start():number.end()]
        string = 'Phone is change'
        return string


@input_error
def show_phone(message):
    message = message.strip().replace('phone ', "")
    phone = list(filter(lambda contact: message.title() in contact['name'], list_contacts))
    if phone:
        string = phone[0]['phone']
        return string
    else:
        raise KeyError


@input_error
def show_all_phone(message):
    strings = []
    for contact in list_contacts:
        strings.append("{} {}".format(contact['name'], contact['phone']))
        string = "\n".join(strings)
    return string


def stop():
    string = 'Good bye!'
    return string


def handler(message):
    message.strip()
    mess = message.split(' ')
    FUNC = {
        'add': add_phone,
        'change': change_phone,
        'phone': show_phone,
        'show': show_all_phone
            }
    if mess[0] in FUNC:
        string = FUNC[mess[0]](message)
        return string
    else:
        main()


print(list_contacts)
def main():
    while True:
        message = input(f'Can I help you?: ')
        message.strip().lower()
        mess = message.split(' ')
        if 'good bye' in message or 'close' in message or 'exit' in message:
            print(stop())
            break
        elif 'hello' in message:
            print(hello())
            continue
        else:
            print(handler(message))
            continue


if __name__ == '__main__':
    main()
