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
