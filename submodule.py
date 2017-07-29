#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Demo logging app submodule
'''
import log
import logging
logger = logging.getLogger("submodule")

logger.debug("loading submodule..")
logger.debug("Path to the submodule's log file: {0}".format(log.logger_filepath(logger = logger, handler_name = "main")))
