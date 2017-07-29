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

# Description

When [`app.py`](https://github.com/stevekm/logging-demo/blob/master/app.py) starts running, the first thing it should do is set up the logging for itself, which will propagate through to subsequent submodule loadings. The file `logging.yml` will be [loaded](https://github.com/stevekm/logging-demo/blob/master/app.py#L23) for configuration, which includes a call back to [`__main__.logpath`](https://github.com/stevekm/logging-demo/blob/master/logging.yml#L16). In this case, it will call the `logpath()` function of `app.py`. This function includes file naming logic, and is a wrapper for the [`logpath()` function in `log.py`](https://github.com/stevekm/logging-demo/blob/master/log.py#L19), which returns a `FileHandler` for the logger object, outputting to the specified file path.

Now that the first `logger` object has been created, we can load submodule(s) which have their own [`logger`  objects](https://github.com/stevekm/logging-demo/blob/master/submodule.py#L8). 

For good measure, we also have a way to [retrieve the file path](https://github.com/stevekm/logging-demo/blob/master/log.py#L37) to the log output, in case we want to do anything with it later. 
