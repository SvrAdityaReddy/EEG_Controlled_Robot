# EEG Controlled Robot

For collecting the EEG signals we had used the OpenBCI's kit and we had used gopigo robot based on raspberrypi 3 for our experiments.

## Data Collection

The OpenBCI EEG kit can be connected to Laptop via bluetooth dongle. The OpenBCI GUI can be used to write the raw EEG values received from kit to a file which can be used for further processing.

## Data transmission between Laptop and Robot

Client-Server architecture has been used to exchange data between Laptop and robot. A server code is run on gopigo robot which is based on Linux. A client code which runs on Laptop which is based on Linux, captures data written to file from GUI and tranfer it to server running on gopigo robot. The codes specific to client and server can found under [main](https://github.com/SvrAdityaReddy/EEG_Controlled_Robot/tree/master/main) directory and are named as [read_data_file_client.py](https://github.com/SvrAdityaReddy/EEG_Controlled_Robot/blob/master/main/read_data_file_client.py), [robot_server.py](https://github.com/SvrAdityaReddy/EEG_Controlled_Robot/blob/master/main/robot_server.py) respectively.

## Controlling Robot with blink of an Eye

The goal of this experiment is to detect blink of an eye from EEG signal collected from FP1 area in real time and move the robot forward (f) on blink, stop (s) the robot on next blink, again forward (f) on next blink, again stop(s) on next blink and so on.

The blink is detected from EEG signal as follow. <br>

1. The absolute current sample value is subtracted from the mean of previous 8 absolute sample values.
2. If the absolute deviation of the absolute current sample value is subtracted from the mean of previous 8 absolute sample values is greater than 100 we detect it as blink