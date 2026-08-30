import time

TOTAL_PROCESSES = 5
TOTAL_ROUNDS = 10
DELAY = 1


def main():

    token = 0

    print("TOKEN RING MUTUAL EXCLUSION SIMULATION")
    print(f"Processes: {TOTAL_PROCESSES}")
    print(f"Token passes: {TOTAL_ROUNDS}")

    for round_no in range(1, TOTAL_ROUNDS + 1):

        print("\n" + "=" * 50)
        print(f"ROUND {round_no}")
        print("=" * 50)

        print(
            f"Token is currently with Process {token}"
        )

        print(
            f"Process {token} "
            f"ENTERS Critical Section"
        )

        time.sleep(DELAY)

        print(
            f"Process {token} "
            f"EXITS Critical Section"
        )

        next_token = (
            (token + 1) % TOTAL_PROCESSES
        )

        print(
            f"Token passed from Process {token} "
            f"to Process {next_token}"
        )

        token = next_token

    print("\nSimulation completed.")


if __name__ == "__main__":
    main()
