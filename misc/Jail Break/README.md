# Prison Break

Author: [Ting Hui](https://github.com/ChanTingHui)

## Description

This is a python jail challenge.

## Requirements

- Docker: [Dockerfile](./Dockerfile)
- Basic Python.

## Sources

```
Someone is in jail. Break him out of Jail.
```

## Exploit
This is a classic jail challenge where some builtins have been blocked, such as import, exec, file, quit, execfile, etc. We can tell the program is running on python2 as when doing a 'print 1+1' without '()' it provides an output. We can find out that 'print dir()' is allowed abnd with that we can do a 'print dir(__builtins__)' to see the allowed functions. From that, we can see that __dict__ is allowed. So we can make use of __class__ to find the class, __base__ to find the baseclasses and __subclasses__ to show all classess. with that we executed the commands below.
```python
print dict.__class__.__base__.__subclasses__()
```
</br>
The execution provided an output of numerous types in an array and most importantly, it provided '<type 'file'>'. Hence, with that we can try print the flag by using the read function.
```python
print ().__class__.__bases__.__subclasses__()[40]('flag.txt', 'r').read()
```
</br>
We did not get any flags with the provided flag format. However, we were told that the flag is in the source code. But we do not know which file the source code is located in. However, Python creates a __file__ variable for itself when it is about to import a module and the __file__ is a variable that contains the path to the module that is currently being imported. So we can replace 'flag.txt' with __file__
```python
print ().__class__.__bases__.__subclasses__()[40](__file__, 'r').read()
```

<br />

The flag is:

```
wssqrctf{sT3v3_J0b$_fr0m_@ppl3}
```