#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Demo logging app
'''
import os
import log # the app's logging submodule
# path to the current script's dir
scriptdir = os.path.dirname(os.path.realpath(__file__))

def logpath():
    '''
    Return the path to the main log file; needed by the logging.yml
    use this for dynamic output log file paths & names
    '''
    global scriptdir
    # set a timestamped log file for debug log
    scriptname = os.path.basename(__file__)
    script_timestamp = log.timestamp()
    log_file = os.path.join(scriptdir, 'logs', '{0}.{1}.log'.format(scriptname, script_timestamp))
    return(log.logpath(logfile = log_file))

config_yaml = os.path.join(scriptdir, 'logging.yml')
logger = log.log_setup(config_yaml = config_yaml, logger_name = "app")
logger.debug("The app is starting...")

import submodule
