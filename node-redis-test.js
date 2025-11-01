const redis = require('redis');

async function connectRedis() {
    const client = redis.createClient({
        socket: {
            host: 'localhost',
            port: 6379
        },
        password: 'Vipul@12!'  // Change this to test wrong password
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
