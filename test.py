import serial
import time
import logging
import os

log_dir = ("/app/logs")
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, 'hw_test.log')


logging.basicConfig(filename=log_file, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

arduino_port ='/dev/ttyACM0'
baud_rate = 9600

arduino = serial.Serial(arduino_port, baud_rate, timeout=1)

time.sleep(2)


def send_command(command):
    try:
        arduino.write((command + '\n').encode())
        time.sleep(0.1)
    except Exception as e:
        logging.error(f"error while sending command to arduino: {e}")

def read_response():
    response = arduino.readline().decode('utf-8').strip()
    if response:
        return response
    else:
        logging.error('no response from arduino')

def measure_distance():
    send_command("MEASURE")
    response = read_response()
    if int(response.split()[1]) > 400:
        print('error')
        logging.error(f"distance out of range: {response}")
    else:
        print('success')
        logging.info(f"measurement captured from ultrasonic sensor: {response}")

def turn_fan_on():
    send_command("FAN_ON")
    time.sleep(0.5)
    response = read_response()
    if response != 'Fan is ON.':
        print('error')
        logging.error(f"fan not in ON state: current state = {response}") 
    else:
        print('sucess')
        logging.info(f"fan turned on")

def turn_fan_off():
    send_command("FAN_OFF")
    time.sleep(0.5)
    response = read_response()
    if response != 'Fan is OFF.':
        logging.error(f"fan not in OFF state: current state = {response}")
    else:
        logging.info(f"fan turned off{response}")

def user_test_choice():
    print('please choose an option')
    print('1: test ultrasonic sensor measurement device')
    print('2: test fan motor')
    print('3: finish testing')
    choice = int(input("enter 1 or 2 or 3: "))
    return choice

def main():
    while True:
        choice = user_test_choice()

        if choice == 1:
            logging.info('starting measurement test')
            measure_distance()
        elif choice == 2:
            logging.info('starting fan test')
            turn_fan_on()
            time.sleep(5)
            turn_fan_off()
        elif choice == 3:
            arduino.close()
            exit()
        else:
            print('invalid choice. try again')
        print('\n')


if __name__ == "__main__":
    main()

