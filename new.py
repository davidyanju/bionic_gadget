import smbus
import math
import RPi.GPIO as GPIO, time, os

DEBUG = 1
GPIO.setmode(GPIO.BCM)

# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val
def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)
################################################################################################################################
def RCtime (RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.2)

    GPIO.setup(RCpin, GPIO.IN)
    # This takes about 1 millisecond per loop cycle
    while (GPIO.input(RCpin) == GPIO.LOW):
        reading += 1
    return reading
################################################################################################################################
bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
address = 0x68       # This is the address value read via the i2cdetect command

# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(address, power_mgmt_1, 0)

def standBy():
    while fsr_active == true:
        gyro_xout = read_word_2c(0x43)
        gyro_yout = read_word_2c(0x45)
        gyro_zout = read_word_2c(0x47)
        print "gyro data"
        print "---------"
        
        
def actMode():
    print
    print "accelerometer data"
    print "------------------"

    #get acceleration in the x direction
    def get_x_accel():
        return read_word_2c(0x3b) / 16384.0

    #get acceleration in the y direction
    def get_y_accel():
        return read_word_2c(0x3d) / 16384.0

    #get acceleration in the z direction
    def get_z_accel():
        return read_word_2c(0x3f) / 16384.0

    count = 0
    #print "------------ Output Acceleration Data -----------------"
    #while True:
        #for get_y_accel() <
       #print "X: ", get_x_accel(), " Y: ", get_y_accel(), " Z: ", get_z_accel()
       
    print "--------output Acceleration data--------"
    initAclrn = get_y_accel()*100
    if initAclrn < 0:
            initArclrn = 0
    while True:
        newAclrn = get_y_accel()*50
        if newAclrn > initAclrn + 4: #or newAclrn < initAclrn - 0.1:
            print "up",newAclrn
        else:
            print "down",newAclrn

    # standy mode
while True:
    fsr = RCtime(27)
    if fsr = true:
        standBy()
