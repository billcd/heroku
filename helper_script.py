from functions import db
import time

def main():
    print("Saving new number.")
    db.connect()
    db.save_random()


if __name__ == "__main__":
    while True:
        main()
        time.sleep(30)
