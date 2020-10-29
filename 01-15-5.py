import os
import time


def main():
    content = "Our Family has a new member:....Kaiyan(Beam)^_^"
    while True:
        os.system('clear')
        print(content)
        # Hibernate for 200ms
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == "__main__":
    main()
