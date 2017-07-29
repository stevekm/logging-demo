# logging-demo
Python logging demo

This demo shows how to use the `logging` library in Python to give dynamic log file output.

# Example
```
$ ./app.py
[2017-07-29 00:33:01] (app:<module>:26:DEBUG) The app is starting...
[2017-07-29 00:33:01] (app:<module>:27:DEBUG) Path to the app's log file: /data/scripts/log-test/logs/app.py.2017-07-29-00-33-01.log
[2017-07-29 00:33:01] (submodule:<module>:10:DEBUG) loading submodule..
[2017-07-29 00:33:01] (submodule:<module>:11:DEBUG) Path to the submodule's log file: /data/scripts/log-test/logs/app.py.2017-07-29-00-33-01.log
```

# Files
- `app.py`: the main program module
- `submodule.py`: a demo submodule for the program
- `log.py`: a convenience submodule to hold functions used with setting up and interacting with `logging` objects in the program
- `logging.yml`: YAML formatted configuration file for the loggers


