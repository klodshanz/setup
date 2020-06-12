# Hypervisor

It is not possible to run docker and Vagrant on the same Windows setting for the hypervisor, so the setting can be set/unset to support the different technologies

```cmd
bcdedit /set hypervisorlaunchtype off                # Vagrant + Android Emulator
bcdedit /set hypervisorlaunchtype on (or auto start) # Docker
```

# Hibernation

To turn hibernatation on and off and save the space of the ```C:\hiberfil.sys``` in Windows use (cmd as Administrator)

```cmd
powercfg -h off
powercfg -h on
```
