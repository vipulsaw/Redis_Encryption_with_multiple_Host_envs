import redis

def connect_redis():
    try:
        # Change password to test wrong password
        r = redis.Redis(
            host='localhost',
            port=6379,
            password='Vipul@123',  # Change this
            decode_responses=True
        )

        # Test connection
        r.ping()
        print('✅ SUCCESS: Connected to Redis with password!')

        # Test with a simple command
        r.set('test_key', 'Hello Redis')
        value = r.get('test_key')
        print('✅ Test value retrieved:', value)

    except redis.AuthenticationError:
        print('❌ ERROR: Authentication failed - Wrong password')
    except Exception as e:
        print('❌ ERROR:', e)

connect_redis()
