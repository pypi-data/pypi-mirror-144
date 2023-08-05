"""Основной модуль конфигурации и запуска клиента."""

import argparse
import logging
import sys
import os
from Cryptodome.PublicKey import RSA
from PyQt5.QtWidgets import QApplication, QMessageBox

from common.errors import ServerError
from common.decos import log
from common.variables import DEFAULT_IP_ADDRESS, DEFAULT_PORT
from client.database import ClientDatabase
from client.transport import ClientTransport
from client.main_window import ClientMainWindow
from client.start_dialog import UserNameDialog

LOG = logging.getLogger("app.client")


@log
def client_argv():
    """Парсер аргументов командной строки.

    Возвращает кортеж из 4 элементов: адрес сервера, порт, имя пользователя,
    пароль. Выполняет проверку на корректность номера порта.
    """
    argv_parser = argparse.ArgumentParser(
        prog='command_line_client',
        description='аргументы командной строки клиента',
        epilog='автор - Григорьев Сергей'
    )
    argv_parser.add_argument(
        'addr',
        default=DEFAULT_IP_ADDRESS,
        nargs='?',
        help='help')
    argv_parser.add_argument('port', default=DEFAULT_PORT, type=int, nargs='?',
                             help='help')
    argv_parser.add_argument('-n', '--name', default=None, nargs='?',
                             help='help')
    argv_parser.add_argument('-p', '--password', default='', nargs='?',
                             help='help')
    namespace = argv_parser.parse_args(sys.argv[1:])
    server_address = namespace.addr
    server_port = namespace.port
    client_name = namespace.name
    client_passwd = namespace.password

    if not 1023 < server_port < 65536:
        LOG.critical(
            f'Попытка запуска клиента с неподходящим номером порта: '
            f'{server_port}. Допустимы адреса с 1024 до 65535. Клиент '
            f'завершается.')
        # exit(1)
        sys.exit(1)

    return server_address, server_port, client_name, client_passwd


if __name__ == '__main__':
    # Загружаем параметры командной строки
    server_address, server_port, client_name, client_passwd = client_argv()
    LOG.debug('Args loaded')

    # Создаём клиентское приложение
    client_app = QApplication(sys.argv)

    # Если имя пользователя не было указано в командной строке, то запросим его
    start_dialog = UserNameDialog()
    if not client_name or not client_passwd:
        client_app.exec_()
        # Если пользователь ввёл имя и нажал ОК, то сохраняем ведённое и
        # удаляем объект, иначе выходим
        if start_dialog.ok_pressed:
            client_name = start_dialog.client_name.text()
            client_passwd = start_dialog.client_passwd.text()
            LOG.debug(
                f'Using USERNAME = {client_name}, PASSWD = {client_passwd}.')
        else:
            # exit(0)
            sys.exit(0)
    # Записываем логи
    LOG.info(
        f'Запущен клиент с параметрами: адрес сервера: {server_address}, '
        f'порт: {server_port}, имя пользователя: {client_name}')

    # Загружаем ключи с файла, если же файла нет, то генерируем новую пару.
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.getcwd()
    key_file = os.path.join(dir_path, f'{client_name}.key')
    if not os.path.exists(key_file):
        keys = RSA.generate(2048, os.urandom)
        with open(key_file, 'wb') as key:
            key.write(keys.export_key())
    else:
        with open(key_file, 'rb') as key:
            keys = RSA.import_key(key.read())

    # !!!keys.publickey().export_key().
    LOG.debug("Keys successfully loaded.")
    # Создаём объект базы данных
    database = ClientDatabase(client_name)
    # Создаём объект - транспорт и запускаем транспортный поток.
    try:
        transport = ClientTransport(
            server_port,
            server_address,
            database,
            client_name,
            client_passwd,
            keys)
        LOG.debug("Transport ready.")
    except ServerError as error:
        message = QMessageBox()
        message.critical(start_dialog, 'Ошибка сервера', error.text)
        # exit(1)
        sys.exit(1)
    transport.setDaemon(True)
    transport.start()

    # Удалим объект диалога за ненадобностью.
    del start_dialog

    # Создаём GUI.
    main_window = ClientMainWindow(database, transport, keys)
    main_window.make_connection(transport)
    main_window.setWindowTitle(f'Чат Программа alpha release - {client_name}')
    client_app.exec_()

    # Раз графическая оболочка закрылась, закрываем транспорт.
    transport.transport_shutdown()
    transport.join()
