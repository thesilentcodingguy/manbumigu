```bash
nano /home/ubuntu/script.sh
```

```bash
#!/bin/bash
echo "Hello Selcia"
```

```bash
chmod +x /home/ubuntu/script.sh
```

```bash
/home/ubuntu/script.sh
```

```bash
pwd
```

```bash
crontab -e
```

```cron
* * * * * /bin/bash /home/ubuntu/script.sh >> /home/ubuntu/output.txt 2>&1
```

```bash
crontab -l
```

```bash
systemctl status cron
```

```bash
cat /home/ubuntu/output.txt
```

```bash
journalctl -u cron --since "5 minutes ago"
```
