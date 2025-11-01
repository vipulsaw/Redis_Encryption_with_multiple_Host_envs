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
