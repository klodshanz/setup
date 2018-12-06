# Android Snippets

## Set Correct Time For Emulator

The time is reset every time the emulator is launched. To have the emulator mirror the host time on Mac run the command below. The ```emulator-5554``` is the device serial number that is needed when more than one device is active. You can get a list of active devices with ```adb devices```.

```bash
adb -s emulator-5554 shell date -s `date +"%Y%m%d.%H%M%S"`
```
