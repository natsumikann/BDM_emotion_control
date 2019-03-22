import wiringpi as pi, time

def get_value():
    SPI_CH = 0
    READ_CH = 0
    pi.wiringPiSPISetup(SPI_CH, 1000000)
    buffer = 0x6800 | (0x1800 * READ_CH)
    buffer = buffer.to_bytes ( 2, byteorder = 'big')
    pi.wiringPiSPIDataRW(SPI_CH, buffer)
    value = (buffer[0]*256 + buffer[1]) & 0x3ff
    return value

