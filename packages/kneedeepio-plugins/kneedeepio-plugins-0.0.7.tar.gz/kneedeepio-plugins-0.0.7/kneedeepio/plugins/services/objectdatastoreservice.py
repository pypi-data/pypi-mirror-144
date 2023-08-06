#!/usr/bin/env python3

### IMPORTS ###
import abc
import json
import logging

### GLOBALS ###

### FUNCTIONS ###

### CLASSES ###
class ObjectDatastoreService(metaclass = abc.ABCMeta):
    def __init__(self):
        self.logger = logging.getLogger(type(self).__name__)

    @abc.abstractmethod
    def get_value(self, key):
        raise NotImplementedError

    @abc.abstractmethod
    def set_value(self, key, value):
        raise NotImplementedError

class InMemoryObjectDatastoreService(ObjectDatastoreService):
    def __init__(self):
        super().__init__()
        self.logger.debug("Inputs - None")
        self._data = {}

    def get_value(self, key):
        self.logger.debug("Getting value for key: %s - %s", key, self._data[key])
        return self._data[key]

    def set_value(self, key, value):
        self.logger.debug("Setting value for key: %s - %s", key, value)
        self._data[key] = value

class BasicFileBackedObjectDatastoreService(ObjectDatastoreService):
    def __init__(self, filename):
        super().__init__()
        self.logger.debug("Inputs - filename: %s", filename)
        self._filename = filename
        self._data = {}

        self.logger.debug("Loading the contents of the file.")
        try:
            with open(self._filename, mode = 'r', encoding = 'utf8') as input_file:
                self._data = json.loads(input_file.read())
            self.logger.debug("After loading self._data: %s", self._data)
        except FileNotFoundError:
            self.logger.info("File not found when trying to load initial data.")

    def get_value(self, key):
        self.logger.debug("Getting value for key: %s - %s", key, self._data[key])
        return self._data[key]

    def set_value(self, key, value):
        self.logger.debug("Setting value for key: %s - %s", key, value)
        self._data[key] = value
        self.logger.debug("Saving the contents to the file.")
        with open(self._filename, mode = 'w', encoding='utf8') as output_file:
            output_file.write(json.dumps(self._data))
