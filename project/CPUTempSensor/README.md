# CPU Temperature Sensor
A CPU temperature sensor is a component integrated into a computer's central processing unit (CPU) or its motherboard. Its primary function is to monitor and report the temperature of the CPU. This information is crucial because CPUs generate heat during operation, and excessive heat can lead to performance issues or even hardware damage if not properly managed.

Here are some key points about CPU temperature sensors:

1. Location: In modern CPUs, temperature sensors are typically embedded within the CPU die itself. They are designed to measure the temperature at various points on the chip to ensure accurate monitoring.

2. Function: The main function of a CPU temperature sensor is to monitor the temperature of the CPU in real-time. This data is then used by the computer's firmware (BIOS/UEFI) or operating system to adjust fan speeds (via PWM) and manage power consumption to keep the CPU operating within safe temperature limits.

3. Accuracy: Temperature sensors are designed to provide accurate readings under normal operating conditions. However, factors such as ambient temperature, airflow within the computer case, and workload on the CPU can affect the accuracy of these readings.

4. Monitoring: Users can monitor CPU temperature through various software utilities provided by the motherboard manufacturer, third-party software tools, or within the operating system itself. These utilities often display real-time temperature readings and sometimes allow users to set temperature thresholds for automatic actions (like increasing fan speed).

5. Importance: Monitoring CPU temperature is important for several reasons:
	* Performance: Excessive heat can cause the CPU to throttle (reduce performance) to prevent damage.
	* Reliability: High temperatures over prolonged periods can shorten the lifespan of the CPU.
	* Safety: In extreme cases, overheating can cause permanent damage to the CPU or other components.

6. Cooling Solutions: Effective cooling solutions such as heat sinks, fans, liquid cooling, and thermal paste are used to manage CPU temperature and dissipate heat efficiently.

In summary, a CPU temperature sensor plays a critical role in maintaining the stability, performance, and longevity of a computer system by ensuring the CPU operates within safe thermal limits.
So, I want see those information on real-time basis. I use this small piece of python code to achieve it.


## Pre-requisite
* psutil library of python:
```
pip install psutil
```

* Matplotlib for plotting:
```
python -m pip install -U pip
python -m pip install -U matplotlib
```
