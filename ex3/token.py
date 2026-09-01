import time

TOTAL_PROCESSES = 5
DELAY = 1

# Logical ring
processes = [1, 2, 3, 4, 5]

# Processes that requested the Critical Section
requests = [1, 3, 2, 4, 5]


def enter_critical_section(pid):
    print(f"\nProcess {pid} ENTERS Critical Section")

    # Simulate work inside CS
    time.sleep(DELAY)

    print(f"Process {pid} EXITS Critical Section")


def token_ring():
    # Initially token is with P1
    token = 1

    print("=" * 50)
    print("TOKEN RING MUTUAL EXCLUSION")
    print("=" * 50)

    print("\nLogical Ring:")
    print("P1 -> P2 -> P3 -> P4 -> P5 -> P1")

    print("\nRequest Order:")
    print(" -> ".join(f"P{p}" for p in requests))

    print("\nStarting Token: P1")

    # Continue until all requests are completed
    remaining_requests = requests.copy()

    while remaining_requests:

        print("\n" + "-" * 50)
        print(f"Token is currently with Process {token}")
        print("-" * 50)

        # Check whether current process requested CS
        if token in remaining_requests:

            print(f"Process {token} has requested Critical Section")

            # Remove request so it is not processed again
            remaining_requests.remove(token)

            # Enter CS
            enter_critical_section(token)

        else:

            print(
                f"Process {token} has NOT requested "
                f"Critical Section"
            )

            print(
                f"Process {token} simply passes the token"
            )

        # Find next process in the ring
        current_index = processes.index(token)

        next_index = (
            current_index + 1
        ) % TOTAL_PROCESSES

        next_token = processes[next_index]

        print(
            f"Token passed from Process {token} "
            f"to Process {next_token}"
        )

        token = next_token

        time.sleep(DELAY)

    print("\n" + "=" * 50)
    print("All requests have been completed.")
    print("Token Ring simulation completed.")
    print("=" * 50)


if __name__ == "__main__":
    token_ring()
