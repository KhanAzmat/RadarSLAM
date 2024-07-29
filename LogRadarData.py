import serial

# Configure the serial port
serial_port = '/dev/ttyUSB0'  # Serial port
baud_rate = 921600  # Sensor's baud rate

# Open the serial port
ser = serial.Serial(serial_port, baud_rate, timeout=1)

def parse_sensor_data(line):
    """
    Parse a line of sensor data.
    :param line: str --> raw line from the sensor
    :return: dict --> parsed sensor data
    """
    try:
        # Split the line by commas
        parts = line.strip().split(',')
        
        if len(parts) != 4:
            print(f"Unexpected data format: {line}")
            return None
        
        # Extract the values
        identifier = parts[0]
        value1 = int(parts[1])
        value2 = int(parts[2])
        value3 = parts[3]
        
        # Create a dictionary with the parsed data
        data = {
            'identifier': identifier,
            'value1': value1,
            'value2': value2,
            'value3': value3
        }
        
        return data
    except Exception as e:
        print(f"Error parsing line: {line}, error: {e}")
        return None

def read_from_serial():
    """
    Read data from the serial port and parse it.
    """
    while True:
        try:
            # Read a line from the serial port
            line = ser.readline().decode('utf-8').strip()
            if line:
                parsed_data = parse_sensor_data(line)
                if parsed_data:
                    print(parsed_data)
        except Exception as e:
            print(f"Error reading from serial port: {e}")
            break

if __name__ == "__main__":
    try:
        read_from_serial()
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        ser.close()
