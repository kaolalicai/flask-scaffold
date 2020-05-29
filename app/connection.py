"""如果需要启动db链接, 启动此注释, 因为pymongo有读写锁, 如果被gunicorn复制以后, 会导致死锁的情况, 因此需要此功能转换一下"""
# import redis
# import pymongo


class GetClient:
    func_dict = {
        # 'mongodb': lambda: pymongo.MongoClient('mongodb://localhost:27017')['admin'],
        # 'redis': lambda: redis.Redis(
        #     connection_pool=redis.ConnectionPool.from_url('redis://localhost:63741', decode_responses=True)
        # )
    }

    def __init__(self, client_name: str):
        self.client = None
        self.client_name = client_name

    def _start(self):
        if self.client is None:
            self.client = self.func_dict[self.client_name]()
        return self.client

    def __getattr__(self, attr: str):
        conn = self._start()
        return conn.__getattribute__(attr)

    def __getitem__(self, item: str):
        conn = self._start()
        return conn.__getitem__(item)


class DBConnections:
    """
    管理DB启动
    使用方法:
    from app.connection import DBConnections
    db = DBConnections.mongodb
    users = list(db.user.find())
    """
    # mongodb = GetClient('mongodb')
    # redis = GetClient('redis')

