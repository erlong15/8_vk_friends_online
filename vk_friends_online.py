import vk
import getpass

APP_ID = 6216998


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    try:
        api = vk.API(session)
    except vk.exceptions.VkAuthError:
        raise
    return api.users.get(user_ids=api.friends.getOnline())


def output_friends_to_console(friends_online):
    output = "{first_name} {last_name}"
    for friend in friends_online:
        print(output.format(**friend))


if __name__ == '__main__':
    login = input('input your vk login: ')
    password = getpass.getpass("input your pass: ")
    try:
        friends_online = get_online_friends(login, password)
        output_friends_to_console(friends_online)
    except vk.exceptions.VkAuthError as e:
        print(str(e))
