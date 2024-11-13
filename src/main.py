from logger.logger_singleton import Logger
from logger.handler_factory import LogHandlerFactory
import os


def ensure_log_directory():
    if not os.path.exists('logs'):
        os.makedirs('logs')


def main():
    ensure_log_directory()

    logger = Logger()


    console_handler = LogHandlerFactory.create_handler("console")
    file_handler = LogHandlerFactory.create_handler("file", filename="logs/app.log")
    json_handler = LogHandlerFactory.create_handler("json", filename="logs/app.json")

    logger.add_handler(console_handler)
    logger.add_handler(file_handler)
    logger.add_handler(json_handler)

    logger.log("Application started", "INFO")
    logger.log("Processing data...", "DEBUG")
    logger.log("An error occurred!", "ERROR")

    another_logger = Logger()
    another_logger.log("This message will be logged to all handlers")


    print("Same logger instance:", logger is another_logger)


if __name__ == "__main__":
    main()