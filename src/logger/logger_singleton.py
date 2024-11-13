class Logger:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not Logger._initialized:
            self.log_handlers = []
            Logger._initialized = True

    def add_handler(self, handler):
        self.log_handlers.append(handler)

    def log(self, message, level="INFO"):
        for handler in self.log_handlers:
            handler.write(f"[{level}] {message}")