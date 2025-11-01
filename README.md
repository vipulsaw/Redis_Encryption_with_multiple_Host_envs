# Redis_Encryption_with_multiple_Host_envs

## Redis Installation on Ubuntu 22.04
```
apt update
```
```
sudo apt install redis-server
```
```
sudo systemctl start redis-server
```
```
sudo systemctl enable redis-server
```
```
sudo systemctl status redis-server
```

## Set Encryption in Conf file

### vim /etc/redis/redis.conf
### /requirepass  ##  serach requirepass
### then uncomment it and put Enter password
<img width="306" height="218" alt="image" src="https://github.com/user-attachments/assets/edf1c9fb-71c7-407e-b8b9-f4fe2d5bc448" />

```
sudo systemctl restart redis-server
```

## Method A: Using redis-cli with password flag
```
redis-cli -a Vipul@123!
```
<img width="598" height="59" alt="image" src="https://github.com/user-attachments/assets/e2566269-c7c0-4352-b43a-02e6f35b2fe4" />

## Method B: Authenticate after connecting
```
redis-cli

127.0.0.1:6379> AUTH Vipul@123!
OK
127.0.0.1:6379> ping
PONG
```
<img width="407" height="86" alt="image" src="https://github.com/user-attachments/assets/47c3ea1a-8390-4b9d-a49a-ddb347c1676a" />

## Nodejs Installation and Testing
```
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
```
```
sudo apt install nodejs -y
```
<img width="325" height="20" alt="image" src="https://github.com/user-attachments/assets/157c398f-d963-4c02-b0a3-5afea66466dc" />

```
npm install redis
```
```
node-redis-test.js
```

```
const redis = require('redis');

async function connectRedis() {
    const client = redis.createClient({
        socket: {
            host: 'localhost',
            port: 6379
        },
        password: 'Vipul@123!'  // Change this to test wrong password
    });

    try {
        await client.connect();
        console.log('✅ SUCCESS: Connected to Redis with password!');

        // Test with a simple command
        await client.set('test_key', 'Hello Redis');
        const value = await client.get('test_key');
        console.log('✅ Test value retrieved:', value);

    } catch (error) {
        console.log('❌ ERROR:', error.message);
    } finally {
        await client.quit();
    }
}

connectRedis();
```
<img width="380" height="79" alt="image" src="https://github.com/user-attachments/assets/ae6b66bf-90e3-4a60-aa9f-f1aafef3731b" />

## Python Installation and Testing
```
sudo apt install python3 python3-pip python3-venv -y
```
```
sudo apt install python3-redis -y
```
```
vim python-redis-test.py
```

```
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
```

```
python3 python-redis-test.py
```

<img width="353" height="83" alt="image" src="https://github.com/user-attachments/assets/eefc3708-a881-420d-8104-aa2d1e13cdb5" />






