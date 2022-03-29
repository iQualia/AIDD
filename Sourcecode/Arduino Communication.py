import serial
import time

ser = serial.Serial('COM3',9600)
time.sleep(2)

while True:
    b = ser.readline()         # read a byte string
    string_n = b.decode() # decode byte string into Unicode
    print(string_n)
    string = string_n.rstrip() # remove \n and \r
    flt = float(string)        # convert string to float
    print(flt)
    if flt == 1:    #once the data received from arduino is the same start recording sound and process it
        print('Starts Tapping')

ser.close()







#serialport = serial.Serial(port="COM3", baudrate = 9600)
#while(True):

   #if(serialport.in_waiting>0):
   #     string=serialport.readline()
      #  print(string)


#Set a timer and Terminal High


# Before send the terminal high, send signal to python

# python receive then start recording immediately
