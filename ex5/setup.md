## Part 1 — Virtual Instances Management

### VM1 / Existing Ubuntu VM

```bash
sudo apt update
```

```bash
sudo apt install apache2 -y
```

```bash
sudo systemctl enable apache2
```

```bash
sudo systemctl start apache2
```

```bash
sudo systemctl status apache2
```

```bash
ifconfig
```

```bash
sudo nano /var/www/html/index.html
```

```html
<!DOCTYPE html>
<html>
<head>
    <title>VM1</title>
</head>
<body>
    <h1>Hello from VM1</h1>
</body>
</html>
```

---

### VM2 — Cloned VM

```bash
sudo apt update
```

```bash
sudo apt install apache2 -y
```

```bash
sudo systemctl enable apache2
```

```bash
sudo systemctl start apache2
```

```bash
sudo systemctl status apache2
```

```bash
ifconfig
```

```bash
sudo nano /var/www/html/index.html
```

```html
<!DOCTYPE html>
<html>
<head>
    <title>VM2</title>
</head>
<body>
    <h1>Hello from VM2</h1>
</body>
</html>
```

---

### VM3 — Cloned VM

```bash
sudo apt update
```

```bash
sudo apt install apache2 -y
```

```bash
sudo systemctl enable apache2
```

```bash
sudo systemctl start apache2
```

```bash
sudo systemctl status apache2
```

```bash
ifconfig
```

```bash
sudo nano /var/www/html/index.html
```

```html
<!DOCTYPE html>
<html>
<head>
    <title>VM3</title>
</head>
<body>
    <h1>Hello from VM3</h1>
</body>
</html>
```

---

# Part 2 — HAProxy Load Balancer

### On Load Balancer VM

```bash
sudo apt update
```

```bash
sudo apt install haproxy -y
```

```bash
sudo nano /etc/haproxy/haproxy.cfg
```

Add:

```text
frontend http_front
    bind *:80
    default_backend http_back

backend http_back
    balance roundrobin
    server vm1 <VM1_IP>:80 check
    server vm2 <VM2_IP>:80 check
    server vm3 <VM3_IP>:80 check
```

### Find VM IPs

On VM1:

```bash
ifconfig
```

On VM2:

```bash
ifconfig
```

On VM3:

```bash
ifconfig
```

Replace:

```text
<VM1_IP>
<VM2_IP>
<VM3_IP>
```

with the actual IP addresses.

### Validate HAProxy configuration

```bash
sudo haproxy -c -f /etc/haproxy/haproxy.cfg
```

### Restart and enable HAProxy

```bash
sudo systemctl restart haproxy
```

```bash
sudo systemctl enable haproxy
```

```bash
sudo systemctl status haproxy
```

### Find Load Balancer IP

```bash
ifconfig
```

### Test each Apache server

```bash
curl http://<VM1_IP>
```

```bash
curl http://<VM2_IP>
```

```bash
curl http://<VM3_IP>
```

### Test Load Balancer

```bash
curl http://<LOAD_BALANCER_IP>
```

```text
http://<LOAD_BALANCER_IP>
```

### Test failover

Stop Apache on VM1:

```bash
sudo systemctl stop apache2
```

Then from the Load Balancer VM:

```bash
curl http://<LOAD_BALANCER_IP>
```

Restart VM1:

```bash
sudo systemctl start apache2
```

Check HAProxy:

```bash
sudo systemctl status haproxy
```
