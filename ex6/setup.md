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

### 1. Create the CPU-intensive script

```
nano /home/ubuntu/script1.sh
```

```
#!/bin/bash
echo "CPU-intensive task started at $(date)"
for i in {1..1000000}; do
    result=$((i * i))
done
echo "CPU-intensive task completed at $(date)"
```

```
chmod +x /home/ubuntu/script1.sh
```

```
/home/ubuntu/script1.sh
```

### 2. Create the lightweight script

```
nano /home/ubuntu/script2.sh
```

```
#!/bin/bash
echo "System information logged at $(date)"
uptime
free -h
```

```
chmod +x /home/ubuntu/script2.sh
```

```
/home/ubuntu/script2.sh
```

### 3. Schedule Cron Jobs with Different Nice Values

```
crontab -e
```

```
* * * * * /usr/bin/nice -n 10 /bin/bash /home/ubuntu/script1.sh >> /home/ubuntu/script1.log 2>&1
* * * * * /usr/bin/nice -n 0 /bin/bash /home/ubuntu/script2.sh >> /home/ubuntu/script2.log 2>&1
```

### 4. Verify Cron Jobs

```
crontab -l
```

```
systemctl status cron
```

```
cat /home/ubuntu/script1.log
```

```
cat /home/ubuntu/script2.log
```

```
journalctl -u cron --since "5 minutes ago"
```

### 5. Verify Process Priorities

```
ps -eo pid,ni,comm | grep -E 'script1|script2'
```

```
top
```

Expected result: `script1.sh` runs with nice value `10` (lower CPU scheduling priority), while `script2.sh` runs with nice value `0` (normal priority).

Note: Cron runs both jobs every minute. Nice values influence CPU scheduling priority, but do not guarantee that one task receives CPU time only when the system is idle.
