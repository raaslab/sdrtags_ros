#!/usr/bin/python

import matplotlib.pyplot as plt
from rtlsdr import *
import rospy
from sdrtags_ros.msg import *
from scipy import signal
import numpy as np

CENTER_FREQ = 96e6
SAMPLE_RATE = 2.4e6
GAIN = 4
PUB_RATE = 1
WIDTH = 10	# width in Hz of the peak
PLOT = True 

def init():

	sdr = RtlSdr()

	# configure device
	sdr.sample_rate = SAMPLE_RATE
	sdr.center_freq = CENTER_FREQ 
	sdr.gain = GAIN

	# configure ROS stuff
	rospy.init_node('sdrtag')
	detections_pub = rospy.Publisher('sdr/detections', SDRTagDetections, queue_size = 10)

	rate = rospy.Rate(PUB_RATE)

	while not rospy.is_shutdown():
		samples = sdr.read_samples(256*1024)
		[psd, freq] = plt.psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
		peaks = signal.find_peaks_cwt(psd, np.array([[WIDTH]]))

		# Publish detections
		detections = SDRTagDetections()
		for peak in peaks:
			detection = SDRTagDetection()
			detection.freq = freq[peak]	
			detection.psd = psd[peak]
			detections.detections.append(detection)
		detections_pub.publish(detections)

		# Optional display	
		if PLOT:	
			plt.hold(True)
			plt.xlabel('Frequency (MHz)')
			plt.ylabel('Relative power (dB)')
			plt.plot(freq[peaks],10*np.log10(abs(psd[peaks])),'rs', markersize=20, markerfacecolor='r')
			plt.pause(0.0001)
			plt.hold(False)
		
		rate.sleep()



if __name__ == '__main__':
	try:
		init()
	except rospy.ROSInterruptException:
		pass
