class Process:

    def __init__(self, pid, total_processes):
        self.pid = pid
        self.vector = [0] * total_processes

    # Internal Event
    def event(self, event_name):

        self.vector[self.pid - 1] += 1

        print(
            f"Process {self.pid}: "
            f"{event_name}"
        )

        print(
            f"Vector Clock = "
            f"{self.vector}\n"
        )

    # Send Message
    def send_message(self, receiver, message):

        self.vector[self.pid - 1] += 1

        print(
            f"Process {self.pid} "
            f"SENDS '{message}' "
            f"to Process {receiver.pid}"
        )

        print(
            f"Vector Sent = "
            f"{self.vector}\n"
        )

        receiver.receive_message(
            message,
            self.vector.copy()
        )

    # Receive Message
    def receive_message(
        self,
        message,
        received_vector
    ):

        # Merge vectors
        for i in range(len(self.vector)):

            self.vector[i] = max(
                self.vector[i],
                received_vector[i]
            )

        # Increment receiver's own entry
        self.vector[self.pid - 1] += 1

        print(
            f"Process {self.pid} "
            f"RECEIVES '{message}'"
        )

        print(
            f"Received Vector = "
            f"{received_vector}"
        )

        print(
            f"Updated Vector Clock = "
            f"{self.vector}\n"
        )


# Create three processes
P1 = Process(1, 3)
P2 = Process(2, 3)
P3 = Process(3, 3)


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
