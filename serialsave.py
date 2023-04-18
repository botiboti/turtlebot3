#!/usr/bin/env python3

# Robot kontroller a pwm_mode-hoz
import serial

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
    ser.reset_input_buffer()

    # k inicializalas
    ser.write(b"10.0\n")
    # a inicializalas
    ser.write(b"4\n")
    # tau inicializalas
    ser.write(b"1000.0\n")
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)