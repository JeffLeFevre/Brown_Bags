import time

from contextlib import contextmanager

from pymongo import MongoClient



@contextmanager
def time_print(task_name):
    """
    :param task_name: (string) name of the task for which you want to
    measure how much time it takes to run.

    This example demonstrates use of the context manager decorator.
    """
    t = time.time()
    try:
        yield
    finally:
        msg = "{0} took {1} seconds.".format(task_name, (time.time() - t))
        print(msg)


print("Getting ready to time a task.")
with time_print("Example task"):
    time.sleep(5)


# Multiple context managers can be used in the same with statement:
# with a(x, y) as A, b(z) as B:
#   Do stuff


class File(object):
    """
    Note that this class duplicates python's built in 'open' function
    """
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hola!')


class MongoDBConnection(object):
    """
    An example database connection context manager. Note that some DB libraries
    already implement context managers for connectivity.
    """
    def __init__(self, host='localhost', port='27017'):
        self.host = host
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.host, self.port)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


mongo = MongoDBConnection()
with mongo:
    collection = mongo.connection.MyDbName.Customers
    customer = collection.find({'_id': 123})
    print(customer.get('name'))
