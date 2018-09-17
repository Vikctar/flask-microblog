import os


class Config(object):
    """
    The SECRET_KEY config is a very important item. It's used as cryto
    key, in the defence against CSRF (Cross-Site Request Forgery).
    The app will look in the os environment for a corresponding value. If not found
    a hardcoded value is used instead. This is for dev environment purposes only.

    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
