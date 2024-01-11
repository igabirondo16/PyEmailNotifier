from dotenv import dotenv_values
from py_email_notifier.decorators import send_result_email

secret_info = dotenv_values("./../.env")

def test():
    a = [1,2]
    print(a[3])

@send_result_email(
    sender_email=secret_info.get("SENDER_EMAIL"),
    receiver_email=secret_info.get("RECEIVER_EMAIL"),
    password=secret_info.get("PASSWORD")
)
def main():
    print("Python script for testing PyEmailNotifier")
    test()

if __name__ == "__main__":
    main()