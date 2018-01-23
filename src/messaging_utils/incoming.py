from service_utilitities.connections.base_connection import ConnectionFactory



class IncomingQueue(object):
    def __init__(self, host=None, port=None, uri=None):
        self.kombu = ConnectionFactory.from_uri(uri)
