import os


#configurando a chave secreta para evitar atques CSRF
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'