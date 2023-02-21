# Disabling Password Authentication on Your Server
```
vi /etc/ssh/sshd_config
:wq!
PasswordAuthentication no
sudo systemctl restart ssh
```
