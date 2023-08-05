"""Модуль базы данных сервера."""

import datetime
from sqlalchemy import create_engine, Table, Text, Column, String, Integer, \
    MetaData, DateTime, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.sql import default_comparator


class ServerStorage:
    """Класс - оболочка для работы с базой данных сервера.

    Использует SQLite базу данных, реализован с помощью
    SQLAlchemy ORM и используется классический подход.
    """
    class AllUsers:
        """Класс - отображение таблицы всех пользователей."""

        def __init__(self, username, passwd_hash):
            self.name = username
            self.last_login = datetime.datetime.now()
            self.passwd_hash = passwd_hash
            self.pubkey = None
            self.id = None

    class ActiveUsers:
        """Класс - отображение таблицы активных пользователей."""

        def __init__(self, user_id, ip_address, port, login_time):
            self.user = user_id
            self.ip_address = ip_address
            self.port = port
            self.login_time = login_time
            self.id = None

    class LoginHistory:
        """Класс - отображение таблицы истории входов."""

        def __init__(self, name, date, ip, port):
            self.id = None
            self.name = name
            self.date_time = date
            self.ip = ip
            self.port = port

    class UsersContacts:
        """Класс - отображение таблицы контактов пользователей."""

        def __init__(self, user, contact):
            self.id = None
            self.user = user
            self.contact = contact

    class UsersHistory:
        """Класс - отображение таблицы истории действий."""

        def __init__(self, user):
            self.id = None
            self.user = user
            self.sent = 0
            self.accepted = 0

    def __init__(self, path):
        # Создаём движок базы данных.
        print(path)
        self.database_engine = create_engine(
            f'sqlite:///{path}',
            echo=False,
            pool_recycle=7200,
            connect_args={
                'check_same_thread': False})

        # Получение посредника (metadata)
        self.metadata = MetaData()
        # Создание самих таблиц для БД.
        # Создаём таблицу пользователей.
        users_table = Table('Users', self.metadata,
                            Column('id', Integer, primary_key=True),
                            Column('name', String, unique=True),
                            Column('last_login', DateTime),
                            Column('passwd_hash', String),
                            Column('pubkey', Text)
                            )

        # Создаём таблицу активных пользователей.
        active_users_table = Table('Active_users', self.metadata,
                                   Column('id', Integer, primary_key=True),
                                   Column('user', ForeignKey('Users.id'),
                                          unique=True),
                                   Column('ip_address', String),
                                   Column('port', Integer),
                                   Column('login_time', DateTime)
                                   )

        # Создаём таблицу истории входов.
        user_login_history = Table('Login_history', self.metadata,
                                   Column('id', Integer, primary_key=True),
                                   Column('name', ForeignKey('Users.id')),
                                   Column('date_time', DateTime),
                                   Column('ip', String),
                                   Column('port', Integer)
                                   )

        # Создаём таблицу контактов пользователей.
        contacts = Table('Contacts', self.metadata,
                         Column('id', Integer, primary_key=True),
                         Column('user', ForeignKey('Users.id')),
                         Column('contact', ForeignKey('Users.id'))
                         )

        # Создаем таблицу истории пользователей.
        users_history_table = Table('History', self.metadata,
                                    Column('id', Integer, primary_key=True),
                                    Column('user', ForeignKey('Users.id')),
                                    Column('sent', Integer),
                                    Column('accepted', Integer)
                                    )

        #  миграция всех таблиц.
        self.metadata.create_all(self.database_engine)
        # объединяем python-сущности таблиц и таблицы в БД.
        mapper(self.AllUsers, users_table)
        mapper(self.ActiveUsers, active_users_table)
        mapper(self.LoginHistory, user_login_history)
        mapper(self.UsersContacts, contacts)
        mapper(self.UsersHistory, users_history_table)

        # создание класса сессии и получение объекта сессии.
        session = sessionmaker(bind=self.database_engine)
        self.session = session()

        # Если в таблице активных пользователей есть записи, то их необходимо
        # удалить.
        self.session.query(self.ActiveUsers).delete()
        # подтверждаем запрос на удаление
        self.session.commit()

    def user_login(self, username, ip_address, port, key):
        """Метод обработки данных при входе пользователя.

        Записывает в базу факт входа, обновляет открытый ключ пользователя
        при его изменении.
        """
        # Проверка, есть ли пользователь в таблице пользователей БД.
        result = self.session.query(self.AllUsers).filter_by(name=username)
        # Если имя пользователя уже присутствует в таблице, обновляем время
        # последнего входа и проверяем корректность ключа. Если клиент прислал
        # новый ключ, сохраняем его.

        if result.count():
            user = result.first()
            user.last_login = datetime.datetime.now()
            if user.pubkey != key:
                user.pubkey = key
        # Если нет, то генерируем исключение
        else:
            raise ValueError('Пользователь не зарегистрирован.')
        # Теперь можно создать запись в таблицу активных пользователей о факте
        # входа.

        new_active_user = self.ActiveUsers(user.id, ip_address, port,
                                           datetime.datetime.now())
        self.session.add(new_active_user)
        # плюс сохраняем историю входов через экземпляр класса LoginHistory
        history = self.LoginHistory(user.id, datetime.datetime.now(),
                                    ip_address, port)
        self.session.add(history)

        # и сохранить в историю входов
        history = self.LoginHistory(
            user.id, datetime.datetime.now(), ip_address, port)
        self.session.add(history)
        # сохраняем изменения
        self.session.commit()

    def add_user(self, name, passwd_hash):
        """Регистрирует пользователя. Принимает имя и хэш пароля, создаёт
        запись в таблице статистики.
        """
        user_row = self.AllUsers(name, passwd_hash)
        self.session.add(user_row)
        self.session.commit()
        history_row = self.UsersHistory(user_row.id)
        self.session.add(history_row)
        self.session.commit()

    def remove_user(self, name):
        """Удаляет пользователя из базы."""
        user = self.session.query(self.AllUsers).filter_by(name=name).first()
        self.session.query(self.ActiveUsers).filter_by(user=user.id).delete()
        self.session.query(self.LoginHistory).filter_by(name=user.id).delete()
        self.session.query(self.UsersContacts).filter_by(user=user.id).delete()
        self.session.query(
            self.UsersContacts).filter_by(contact=user.id).delete()
        self.session.query(self.UsersHistory).filter_by(user=user.id).delete()
        self.session.query(self.AllUsers).filter_by(name=name).delete()
        self.session.commit()

    def get_hash(self, name):
        """Получает хэш пароля пользователя."""
        user = self.session.query(self.AllUsers).filter_by(name=name).first()
        return user.passwd_hash

    def get_pubkey(self, name):
        """Получает публичный ключ пользователя."""
        user = self.session.query(self.AllUsers).filter_by(name=name).first()
        return user.pubkey

    def check_user(self, name):
        """Проверяет существование пользователя."""
        if self.session.query(self.AllUsers).filter_by(name=name).count():
            return True
        else:
            return False

    def user_logout(self, username):
        """Фиксирует отключение пользователя."""
        # Запрашиваем пользователя, что покидает нас
        user = self.session.query(self.AllUsers).filter_by(
            name=username).first()
        # удаляем его из таблицы ActiveUsers
        self.session.query(self.ActiveUsers).filter_by(user=user.id).delete()
        self.session.commit()

    # функция, возвращающая список пользователей и время их входа
    def process_message(self, sender, recipient):
        """Записывает в таблицу статистики факт передачи сообщения."""
    #  Получаем ID отправителя и получателя.
        sender = self.session.query(
            self.AllUsers).filter_by(
            name=sender).first().id

        recipient = self.session.query(self.AllUsers).filter_by(
            name=recipient).first().id
    # Запрашиваем строки из истории и увеличиваем счётчики.
        sender_row = self.session.query(
            self.UsersHistory).filter_by(
            user=sender).first()
        sender_row.sent += 1
        recipient_row = self.session.query(self.UsersHistory).filter_by(
            user=recipient).first()
        recipient_row.accepted += 1
        self.session.commit()

    #  Добавляем контакт для пользователя.
    def add_contact(self, user, contact):
        """Добавляет контакт для пользователя."""
        # Получаем ID пользователей.
        user = self.session.query(self.AllUsers).filter_by(name=user).first()
        contact = self.session.query(self.AllUsers).filter_by(
            name=contact).first()

    # Проверяем что не дубль и что контакт может существовать (полю
        # пользователь мы доверяем).
        if not contact or self.session.query(self.UsersContacts).filter_by(
                user=user.id, contact=contact.id).count():
            return

        # Создаём объект и заносим его в базу.
        contact_row = self.UsersContacts(user.id, contact.id)
        self.session.add(contact_row)
        self.session.commit()

    # Удаляем контакт из БД.
    def remove_contact(self, user, contact):
        """Удаляет контакт пользователя."""
        user = self.session.query(self.AllUsers).filter_by(name=user).first()
        contact = self.session.query(self.AllUsers).filter_by(
            name=contact).first()
        # Проверяем что контакт может существовать (полю пользователь мы
        # доверяем).
        if not contact:
            return

        # Удаляем требуемое.
        self.session.query(self.UsersContacts).filter(
            self.UsersContacts.user == user.id,
            self.UsersContacts.contact == contact.id
        ).delete()
        self.session.commit()

    def users_list(self):
        """Возвращает список известных пользователей со временем
        последнего входа.
        """
        query = self.session.query(
            self.AllUsers.name,
            self.AllUsers.last_login
        )
        # Возвращаем список кортежей.
        return query.all()

    def active_users_list(self):
        """Возвращает список активных пользователей."""
        # соединяем таблицы с помощью join и забираем данные
        query = self.session.query(
            self.AllUsers.name,
            self.ActiveUsers.ip_address,
            self.ActiveUsers.port,
            self.ActiveUsers.login_time
        ).join(self.AllUsers)
        # Возвращаем список кортежей
        return query.all()

    def login_history(self, username=None):
        """Возвращает историю входов."""
        # запрос истории ввода
        query = self.session.query(
            self.AllUsers.name,
            self.LoginHistory.date_time,
            self.LoginHistory.ip,
            self.LoginHistory.port
        ).join(self.AllUsers)
        # Если было указано имя пользователя, то фильтруем по нему
        if username:
            query = query.filter(self.AllUsers.name == username)
        return query.all()

    def get_contacts(self, username):
        """Возвращает список контактов пользователя."""
        # Запрашиваем указанного пользователя
        user = self.session.query(self.AllUsers).filter_by(name=username).one()
        # Запрашиваем его список контактов
        query = self.session.query(self.UsersContacts, self.AllUsers.name). \
            filter_by(user=user.id). \
            join(self.AllUsers, self.UsersContacts.contact == self.AllUsers.id)

        # выбираем только имена пользователей и возвращаем их.
        return [contact[1] for contact in query.all()]

    # Функция возвращает количество переданных и полученных сообщений
    def message_history(self):
        """Возвращает статистику сообщений."""
        query = self.session.query(
            self.AllUsers.name,
            self.AllUsers.last_login,
            self.UsersHistory.sent,
            self.UsersHistory.accepted
        ).join(self.AllUsers)
        return query.all()


if __name__ == '__main__':
    test_db = ServerStorage('../server_database.db3')
    # test_db.user_login('test1', '192.168.1.113', 8080)
    # test_db.user_login('test2', '192.168.1.113', 8081)
    print(test_db.users_list())
    # print(test_db.active_users_list())
    # test_db.user_logout('McG')
    # print(test_db.login_history('re'))
    # test_db.add_contact('test2', 'test1')
    # test_db.add_contact('test1', 'test3')
    # test_db.add_contact('test1', 'test6')
    # test_db.remove_contact('test1', 'test3')
    test_db.process_message('test1', 'test2')
    print(test_db.message_history())
