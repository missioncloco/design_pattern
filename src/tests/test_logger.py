import unittest
from logger.logger_singleton import Logger
from logger.handler_factory import LogHandlerFactory


class TestLogger(unittest.TestCase):
    def test_singleton_pattern(self):
        logger1 = Logger()
        logger2 = Logger()
        self.assertIs(logger1, logger2)

    def test_factory_pattern(self):
        console_handler = LogHandlerFactory.create_handler("console")
        file_handler = LogHandlerFactory.create_handler("file", filename="test.log")
        json_handler = LogHandlerFactory.create_handler("json", filename="test.json")

        self.assertIsNotNone(console_handler)
        self.assertIsNotNone(file_handler)
        self.assertIsNotNone(json_handler)
