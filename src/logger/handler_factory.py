from logger.log_handlers import ConsoleLogHandler, FileLogHandler, JSONLogHandler

class LogHandlerFactory:
    @staticmethod
    def create_handler(handler_type, **kwargs):
        if handler_type.lower() == "console":
            return ConsoleLogHandler()
        elif handler_type.lower() == "file":
            return FileLogHandler(kwargs.get('filename', 'app.log'))
        elif handler_type.lower() == "json":
            return JSONLogHandler(kwargs.get('filename', 'app.json'))
        else:
            raise ValueError(f"Unknown handler type: {handler_type}")