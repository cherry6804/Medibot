
from chatterbot.storage.sql_storage import SQLStorageAdapter

class ReadOnlySQLStorageAdapter(SQLStorageAdapter):
    def create(self, *args, **kwargs):
        pass
    def update(self, *args, **kwargs):
        pass
