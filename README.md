# sdrtags_ros

## Dependencies

* librtlsdr-dev ``sudo apt-get install librtlsdr-dev``
* [Matplotlib](https://matplotlib.org) ``pip install -U matplotlib``
* [numpy](https://www.scipy.org/) ``pip install numpy``
* [scipy](https://www.scipy.org/) ``pip install scipy``
* [pyrtlsdr](https://github.com/roger-/pyrtlsdr) ``pip install pyrtlsdr``


## Running the code
* You will also need to blacklist the *dvb_usb_rtl28xxu* kernel module. A quick fix is to disconnect the RTL device from the USB port. Then, remove the module by running the following command ``sudo rmmod dvb_usb_rtl28xxu`` which removes the *dvb_usb_rtl28xxu* module. You may also have to start the *rtl2832_sdr* module by running ``sudo modprobe rtl2832_sdr``. You can check which modules are currently running with ``lsmod | grep rtl``
* Start roscore ``roscore``
* ``rosrun sdrtags_ros psd.py``
