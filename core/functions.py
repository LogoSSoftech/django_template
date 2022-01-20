from core.models import User


def search_username(username):
    '''
    Para evitar que se dupliquen usuarios.
    Si el usuario se está registrando, userData.id = 0

    Si consigue el username, se devuelve True,
    '''
    return True if User.objects.get(username=username) else False
