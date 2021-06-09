from abc import ABC, abstractmethod


class AbstractDBFactory(ABC):
    @abstractmethod
    def create_connection(self) -> 'AbstractDBConnection':
        pass

    @abstractmethod
    def create_migration(self) -> 'AbstractDBMigration':
        pass


class MongoDBFactory(AbstractDBFactory):

    def create_connection(self):
        return MongoDBConnection()

    def create_migration(self):
        return MongoDBMigration()


class MySQLFactory(AbstractDBFactory):

    def create_connection(self):
        return MySQLDBConnection()

    def create_migration(self):
        return MySQLDBMigration()


class AbstractDBConnection(ABC):
    @abstractmethod
    def make_connection(self):
        pass


class MySQLDBConnection(AbstractDBConnection):
    def make_connection(self):
        print('MySQL connection...')


class MongoDBConnection(AbstractDBConnection):
    def make_connection(self):
        print('MongoDB connection...')


class AbstractDBMigration(ABC):
    @abstractmethod
    def make_migrations(self):
        pass


class MySQLDBMigration(AbstractDBMigration):
    def make_migrations(self):
        print('MySql migrations...')


class MongoDBMigration(AbstractDBMigration):
    def make_migrations(self):
        print('MongoDB migrations...')


def handle_db(factory: AbstractDBFactory):
    connection = factory.create_connection()
    migration = factory.create_migration()

    return connection, migration


if __name__ == '__main__':
    mongo_conn, mongo_migration = handle_db(MongoDBFactory())
    mongo_conn.make_connection()
    mongo_migration.make_migrations()

    mysql_conn, mysql_migration = handle_db(MySQLFactory())
    mysql_conn.make_connection()
    mysql_migration.make_migrations()
