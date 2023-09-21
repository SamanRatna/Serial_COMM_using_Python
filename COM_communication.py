import threading
import serial
import serial.tools.list_ports as availablePorts

baud_rate = 9600            # rate of data trandfer


# Thread that handles sender COM
def COM_sender():
    print(SENDER_TAG, "Sender thread is live")

    try:
        # Open a connection
        ser_send = serial.Serial(sender_port, baud_rate)

        if ser_send.is_open:

            print(f"\nConnected to {ser_send.name}. Ready to send data")
            print("Sending from " + sender_port)
            ser_send.write(b'Sending Hello from Sender\n')

            # Close the sending port
            ser_send.close()
            print("\nSerial port for sending closed.")

    except serial.SerialException as e:
        print(f"Error: {e}")


# Thread that handles receiver COM
def COM_receiver():
    print(RECEIVER_TAG, "Receiver thread is live")

    try:
        # Open a connection
        ser_receive = serial.Serial(receiver_port, baud_rate)

        if ser_receive.is_open:
            print(f"\nConnected to {ser_receive.name}. Ready to receive")

            try:
                while True:

                    if (ser_receive.is_open):
                        # Read a line of data from the receiving port
                        received_data = ser_receive.readline()

                        # Print the received data
                        print(
                            f"Received at receiver: {received_data.decode('utf-8')}", end='')
                        # Close the receiving port when done
                        ser_receive.close()
                        print("\nSerial port for receiving closed.")

                    else:
                        return

            except KeyboardInterrupt:
                # Handle Ctrl+C to exit the loop gracefully
                print("Serial data receiving stopped.")

    except serial.SerialException as e:
        print(f"Error: {e}")


# Main Thread
def startCommunicationThread():

    try:
        # Create Sender and Receiver Threads
        senderThread = threading.Thread(target=COM_sender)
        receiverThread = threading.Thread(target=COM_receiver)

        # Start Sender and Receiver Threads
        senderThread.start()
        receiverThread.start()

    except:
        print("Error: Unable to start both threads")


if __name__ == "__main__":

    ports = []

    # Get a list of available serial ports
    available_ports = list(availablePorts.comports())

    # If Port not available then print error and not necessary to start any threads
    if not available_ports:
        print("No serial ports found.")

    # If Ports are available then, print all of them with their status and start the communication threads
    else:
        print("\n***** Available serial ports: *****")
        for port in available_ports:
            print(f"- {port.device}: {port.description}")
            ports.append(port.device)

        sender_port = ports[0]        # PORT number to send data
        receiver_port = ports[1]      # PORT number to receive data

        SENDER_TAG = sender_port + ' ======>'
        RECEIVER_TAG = receiver_port + ' ======>'
        print("")

        startCommunicationThread()
