#!/usr/bin/env python3

### IMPORTS ###
import abc

from kneedeepio.plugins.services import LoggingService

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class Plugin(metaclass = abc.ABCMeta):
    required_services = ["logging"] # NOTE: The logging service is always supplied, but it's good to be explicit.
    def __init__(self, services):
        if isinstance(services["logging"], LoggingService):
            self.logger = services["logging"]
        else:
            raise TypeError("Invalid object passed as Logging Service")
        self.logger.debug("Plugin Initialized: %s", type(self).__name__)

    @abc.abstractmethod
    def setup(self):
        # This method should do whatever is needed to initialize the plugin's operation.
        raise NotImplementedError

    @abc.abstractmethod
    def tick(self):
        # FIXME: Pick a better name for this
        # This method should do some small piece of work for the plugin.
        raise NotImplementedError

    @abc.abstractmethod
    def teardown(self):
        # This method should do whatever is needed to un-setup the plugin, stopping operation.
        raise NotImplementedError
