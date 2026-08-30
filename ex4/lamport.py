class Process:

    def __init__(self, pid):
        self.pid = pid
        self.clock = 0

    # Internal event
    def event(self, event_name):
        self.clock += 1

        print(
            f"Process {self.pid}: "
            f"{event_name} | Clock = {self.clock}"
        )

    # Send message
    def send_message(self, receiver, message):

        self.clock += 1
        timestamp = self.clock

        print(
            f"\nProcess {self.pid} "
            f"SENDS '{message}' "
            f"to Process {receiver.pid}"
        )

        print(f"Timestamp Sent = {timestamp}")

        receiver.receive_message(
            message,
            timestamp
        )

    # Receive message
    def receive_message(
        self,
        message,
        received_timestamp
    ):

        self.clock = max(
            self.clock,
            received_timestamp
        ) + 1

        print(
            f"Process {self.pid} "
            f"RECEIVES '{message}'"
        )

        print(
            f"Received Timestamp = "
            f"{received_timestamp}"
        )

        print(
            f"Updated Clock = "
            f"{self.clock}"
        )


# Create processes
P1 = Process(1)
P2 = Process(2)
P3 = Process(3)


# Internal events
P1.event("Internal Event A")
P2.event("Internal Event B")
P3.event("Internal Event C")


# Message passing
P1.send_message(P2, "Hello P2")
P2.send_message(P3, "Hello P3")
P3.send_message(P1, "Reply to P1")


# More internal events
P1.event("Internal Event D")
P2.event("Internal Event E")
P3.event("Internal Event F")
