
import time
import serial


class HoverCommand:

    SERIAL_PORT = '/dev/ttyUSB0'
    SERIAL_BAUD = 115200
    TIME_SEND = 0.1

    startBytes = bytes.fromhex('ABCD')[::-1]

    def __init__(self) -> None:
        self.uart = serial.Serial(
            self.SERIAL_PORT, self.SERIAL_BAUD, timeout=1)

    def send(self, steer: int, speed: int):
        steerBytes = steer.to_bytes(2, byteorder='little', signed=True)
        speedBytes = speed.to_bytes(2, byteorder='little', signed=True)
        checksum = bytes(a ^ b ^ c for (a, b, c) in zip(
            self.startBytes, steerBytes, speedBytes))
        command = self.startBytes+steerBytes+speedBytes+checksum

        self.uart.write(command)
        print('steer:'+str(steer)+' speed:'+str(speed))
