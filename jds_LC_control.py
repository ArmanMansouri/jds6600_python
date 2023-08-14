# example application to read and change the status of a JDS6600
# connected over USB

# version 0.1 - 20180126
# version 0.2 - 20191007

# kristoff Bonne (ON1ARF)

# import library

import jds6600 # pip install jds6600
from time import sleep

def sweep(fg, ch, s):
    x = 0.1
    for i in range(int((10-0.1)/s)+1):
        fg.set_amplitude(channel=ch, value=x)
        x += s
        sleep(1)


fg = jds6600.JDS6600(port="COM11")
fg.connect()

fg.set_channels(channel1=True, channel2=True)

fg.set_offset(channel=1, value=0)

fg.set_waveform(channel=1, value='square')

fg.set_frequency(channel=1, value=2e3)


sweep(fg, 1, 1)

fg.close()

'''
j.getAPIinfo_version()
j.getAPIinfo_release()



# API information calls
j.getinfo_devicetype()
j.getinfo_serialnumber()

j.getinfo_waveformlist()


# get status of jds6600
j.getchannelenable()

for ch in (1,2):
	j.getwaveform(ch)
	j.getfrequency(ch)
	j.getamplitude(ch)
	j.getoffset(ch)
	j.getdutycycle(ch)

j.getphase()


# changing status
j.setfrequency(1,1000)
j.setfrequency(1,40000,1)

j.setwaveform(2,2)
j.setwaveform(1,"sinc")
'''
'''
import sys
import glob
import serial


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

if __name__ == '__main__':
    print(serial_ports())  
'''