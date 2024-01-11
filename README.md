
## PyEmailNotifier

PyEmailNotifier is a simple Python decorator which is used to email all the content (standard output and standard error) generated by a program to the developer.

Machine Learning and Deep Learning experiments often require long training execution times, which are commonly left running in the background on a server. When those experiments finish (either because the training was successfull or because any kind of exception was raised) the server resources are freed, and the remain unused until the developer sends another task. As the user does not receive any kind of notification, this situation can lead to a highly inefficient management of time and resources.

PyEmailNotifier has been designed to send by email the result of the experiments, so that less time is wasted when any kind of problem occurs.

## Getting started

First, clone the github repository:

```shell
$: git clone https://github.com/igabirondo16/PyEmailNotifier.git
```

After, install the python module in your local virtual environment:

```shell
$: cd ./PyEmailNotifier
$: pip install .
```

Finally, use the module as a common decorator:

```python
from py_email_notifier.decorators import send_result_email

def very_long_program():
    a = [1,2]
    print(a[3])


@send_result_email(
    sender_email="sender@email.com",
    receiver_email="receiver@email.com",
    password="password-of-the-sender-email"
)
def main():
    print("Python script for testing PyEmailNotifier")
    very_long_program()

if __name__ == "__main__":
    main()
```

Notice that for keeping sensible data such as emails or passwords safe, it is **strongly recommended** to take some [security measures](https://blog.gitguardian.com/how-to-handle-secrets-in-python/).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

Apache License 2.0