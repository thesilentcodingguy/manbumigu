import time

TOTAL_PROCESSES = 5
DELAY = 1


class Coordinator:

    def __init__(self):
        self.busy = False

    def request(self, pid):

        print(
            f"Process {pid} -> Coordinator : REQUEST"
        )

        if not self.busy:

            self.busy = True

            print(
                f"Coordinator -> Process {pid} : GRANT"
            )

            return True

        print(
            f"Coordinator -> Process {pid} : WAIT"
        )

        return False

    def release(self, pid):

        print(
            f"Process {pid} -> Coordinator : RELEASE"
        )

        self.busy = False


def main():

    coordinator = Coordinator()

    print("CENTRALIZED MUTUAL EXCLUSION SIMULATION")

    for pid in range(TOTAL_PROCESSES):

        print("\n" + "=" * 50)
        print(f"PROCESS {pid} WANTS TO ENTER CS")
        print("=" * 50)

        while not coordinator.request(pid):
            time.sleep(DELAY)

        print(
            f"Process {pid} "
            f"ENTERS Critical Section"
        )

        time.sleep(DELAY)

        print(
            f"Process {pid} "
            f"EXITS Critical Section"
        )

        coordinator.release(pid)

    print("\nSimulation completed.")


if __name__ == "__main__":
    main()
