#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Demo logging app submodule
'''
import os
import datetime
import logging

# ~~~~~ GLOBALS ~~~~~ #
scriptname = os.path.basename(__file__)
scriptdir = os.path.dirname(os.path.realpath(__file__))
script_timestamp = '{:%Y-%m-%d-%H-%M-%S}'.format(datetime.datetime.now())


# ~~~~~ CUSTOM FUNCTIONS ~~~~~ #
def logger_filepath(logger, handler_name):
    '''
    Get the path to the filehander log file
    '''
    logger.debug("looking for handler_name {0} in logger".format(handler_name))
    log_file = None
    for h in logger.__dict__['handlers']:
        if h.__class__.__name__ == 'FileHandler':
            logname = h.get_name()
            logger.debug("logname is {0}".format(logname))
            if handler_name == logname:
                log_file = h.baseFilename
    return(log_file)

def build_logger(name = None):
    '''
    Create a logger instance
    '''
    import logging

    global scriptname
    global scriptdir
    global script_timestamp

    if name == None:
        name = scriptname

    log_file = os.path.join(scriptdir, 'logs', '{0}.{1}.log'.format(name, script_timestamp))
    email_log_file = os.path.join(scriptdir, 'logs', '{0}.{1}.email.log'.format(name, script_timestamp))

    # create logger instance
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # create file handler which logs info messages
    filelog = logging.FileHandler(log_file)
    filelog.setLevel(logging.INFO)
    filelog.set_name("filelog")

    # create file handler which logs info messages, meant to be used later as the body of an email
    email_filelog = logging.FileHandler(email_log_file)
    email_filelog.setLevel(logging.INFO)
    email_filelog.set_name("email_filelog")

    # create console handler with a lower
    consolelog = logging.StreamHandler()
    consolelog.setLevel(logging.DEBUG)
    consolelog.set_name("consolelog")

    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
    filelog.setFormatter(formatter)
    consolelog.setFormatter(formatter)
    email_filelog.setFormatter(formatter)

    # add the handlers to logger
    logger.addHandler(consolelog)
    logger.addHandler(filelog)
    logger.addHandler(email_filelog)
    return(logger)




# ~~~~~ CUSTOM CLASSES ~~~~~ #
class MyClass(object):
    '''
    Basic demo class
    '''
    def __init__(self, id):
        self.id = str(id)
        self.logger = build_logger(name = self.id)
        self.logger.debug("Started logging for {0}".format(self.id))
        self.logger.debug("Path to the submodule's email_filelog file: {0}".format(logger_filepath(logger = self.logger, handler_name = "email_filelog")))
        self.logger.info("here is an INFO message")




# ~~~~~ SETUP LOGGER ~~~~~ #
logger = build_logger(name = "submodule")
logger.debug("loading submodule..")
logger.debug("Path to the submodule's log file: {0}".format(logger_filepath(logger = logger, handler_name = "filelog")))
logger.info("here is an INFO message")




# ~~~~~ RUN ~~~~~ #
logger.debug("Creating MyClass object with id {0}".format("foo"))
x = MyClass(id = "foo")

logger.debug("Creating MyClass object with id {0}".format("bar"))
y = MyClass(id = "bar")
