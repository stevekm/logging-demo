# logging-demo
Python logging demo

This demo shows how to use the `logging` library in Python to give dynamic log file output.

# Example
```
$ ./app.py
[2017-07-29 00:18:54] (app:<module>:25:DEBUG) The app is starting...
[2017-07-29 00:18:54] (submodule:<module>:8:DEBUG) loading submodule..
```

# Files
- `app.py`: the main program module
- `submodule.py`: a demo submodule for the program
- `log.py`: a convenience submodule to hold functions used with setting up and interacting with `logging` objects in the program
- `logging.yml`: YAML formatted configuration file for the loggers


