import serial, time
import Tkinter as tk

# Simple script that runs a Tkinter window when you can write.
# It will send to an Arduino serial port a value directly related
# to your typing speed. 
# The servo connected to the Arduino board, using typespeed.ino sketch
# will graphically show your typing speed in real time.

SERIALPORT = "/dev/cu.usbmodem1411"
# Set up serial port
try:
    ser = serial.Serial(SERIALPORT, 9600)
except serial.SerialException:
    print "no device connected - exit"
    sys.exit()

ser.write("0")
start_time = time.time()

def onKeyPress(event):
	elapsed = (150 - translate(time.time() - start_time, 0.01, 0.3, 0, 150))
	ser.write(str(int(elapsed)) + "\n")
	global start_time
	start_time = time.time()

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Adjust limits
    if value < leftMin:
    	value = leftMin
    if value > leftMax:
    	value = leftMax

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

root = tk.Tk()
root.geometry('300x200')
text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
text.pack()
root.bind('<KeyPress>', onKeyPress)
root.mainloop()