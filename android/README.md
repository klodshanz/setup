# Android Snippets

## Android Wear Setup

Enable debugging over bluetooth

## Set Correct Time For Emulator

The time is reset every time the emulator is launched. To have the emulator mirror the host time on Mac run this command:

```bash
adb shell date -s `date +"%Y%m%d.%H%M%S"`
```


