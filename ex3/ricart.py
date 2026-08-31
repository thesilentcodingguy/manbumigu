import time

TOTAL_PROCESSES = 3
DELAY = 1


class Process:

    def __init__(self, pid):
        self.pid = pid

    def request_cs(self):

        print("\n" + "=" * 50)
        print(
            f"RICART-AGRAWALA: PROCESS {self.pid} REQUESTS CS"
        )
        print("=" * 50)

        print("\nREQUEST PHASE")

        for receiver in range(TOTAL_PROCESSES):

            if receiver != self.pid:
                print(
                    f"Process {self.pid} -> "
                    f"Process {receiver}: REQUEST"
                )

        print("\nREPLY PHASE")

        for sender in range(TOTAL_PROCESSES):

            if sender != self.pid:
                print(
                    f"Process {sender} -> "
                    f"Process {self.pid}: REPLY"
                )

        print(
            f"\nProcess {self.pid} "
            f"ENTERS Critical Section"
        )

        time.sleep(DELAY)

        print(
            f"Process {self.pid} "
            f"EXITS Critical Section"
        )


def main():

    print(
        "RICART-AGRAWALA MUTUAL "
        "EXCLUSION SIMULATION"
    )

    processes = [
        Process(pid)
        for pid in range(TOTAL_PROCESSES)
    ]

    for process in processes:
        process.request_cs()

    print("\nSimulation completed.")


if __name__ == "__main__":
    main()



import threading
import time
import random

class Process:
    def __init__(self, id, total_processes):
        self.id = id
        self.total_processes = total_processes
        self.timestamp = 0
        self.requested = False
        self.reply_count = 0
        self.lock = threading.Lock()
        self.request_limit = 3
        self.request_count = 0
        self.deferred_requests = []  # Stores requests to reply to later

    def request_critical_section(self):
        if self.request_count < self.request_limit:
            with self.lock:
                self.timestamp += 1
                self.requested = True
                self.reply_count = 0

            print(f"Process {self.id} requesting critical section at timestamp {self.timestamp}.")

            # Broadcast request to all other processes
            for i in range(self.total_processes):
                if i != self.id:
                    processes[i].receive_request(self.id, self.timestamp)

            # Wait until replies are received from all other processes
            while True:
                with self.lock:
                    if self.reply_count == self.total_processes - 1:
                        break
                time.sleep(0.05)

            self.enter_critical_section()
            self.request_count += 1
        else:
            print(f"Process {self.id} has reached its request limit.")

    def receive_request(self, sender_id, sender_timestamp):
        with self.lock:
            # Tie-breaker using (timestamp, process_id)
            our_priority = (self.timestamp, self.id)
            sender_priority = (sender_timestamp, sender_id)

            # Defer reply if this process is requesting/in CS and has higher priority
            if self.requested and our_priority < sender_priority:
                print(f"Process {self.id} queuing request from Process {sender_id} (ts: {sender_timestamp}).")
                self.deferred_requests.append(sender_id)
            else:
                print(f"Process {self.id} sending reply to Process {sender_id}.")
                processes[sender_id].receive_reply(self.id)

    def receive_reply(self, sender_id):
        with self.lock:
            self.reply_count += 1
            print(f"Process {self.id} received reply from Process {sender_id}.")

    def enter_critical_section(self):
        print(f"\n--> Process {self.id} ENTERED critical section.")
        time.sleep(random.uniform(0.5, 1.5))  # Simulate work inside CS
        print(f"<-- Process {self.id} EXITING critical section.\n")
        self.release_critical_section()

    def release_critical_section(self):
        with self.lock:
            self.requested = False

            # Send replies to all deferred requests
            for pid in self.deferred_requests:
                print(f"Process {self.id} sending deferred reply to Process {pid}.")
                processes[pid].receive_reply(self.id)

            self.deferred_requests.clear()

        print(f"Process {self.id} released critical section.")

def process_runner(process):
    while process.request_count < process.request_limit:
        time.sleep(random.uniform(0.5, 1.5))
        process.request_critical_section()

if __name__ == "__main__":
    num_processes = 5
    processes = [Process(i, num_processes) for i in range(num_processes)]

    threads = []
    for process in processes:
        t = threading.Thread(target=process_runner, args=(process,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("All processes have completed their requests.")
