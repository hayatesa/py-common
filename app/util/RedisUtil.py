import redis

if __name__ == '__main__':
    pool = redis.ConnectionPool(host='119.29.94.246', port=6379, decode_responses=True, password='redis272243')
    r = redis.Redis(connection_pool=pool)
    r.set('food', 'beef', px=60000)
    print(r.get('food'))
