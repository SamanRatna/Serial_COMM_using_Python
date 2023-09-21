# Serial Communication using Python

| Supported Targets | Windows 10 | Windows 11 |
| ----------------- | ---------- | ---------- |

## Pre-requisites

### Softwares

- Python 3.9 or above
- VS Studio Code
- Virtual Serial Port Driver Pro Software

### Libraries

```
$ pip3 install pySerial

(Note: 'Threading' library is used for multithreading. It is built into Python itself.
Consider updating the library if necessary)
```

## Execution

Open 'Virtual Serial Port Driver Pro'. Select 'Pair', choose the names of COM ports, and click 'Create' to confirm a connection.
When successfully paired, it should look like this.
![image](https://github.com/SamanRatna/Serial_COMM_using_Python/assets/46080827/c492ed89-30db-487b-bded-31ec03c8a8ba)


```
$ git clone https://github.com/SamanRatna/Serial_COMM_using_Python
$ python3 COM_communication.py
```

## Result

![image](https://github.com/SamanRatna/Serial_COMM_using_Python/assets/46080827/bcc4d1a4-5159-48dc-80c7-6efaabe5c447)

