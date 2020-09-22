from notifications.providers.telegram import TelegramHandler
from utils.logger import log


class NotificationHandler:
    def __init__(self):
        log.info("Initializing notification handlers")
        self.telegram_handler = TelegramHandler()
        log.info(f"Enabled Handlers: {self.get_enabled_handlers()}")

    def get_enabled_handlers(self):
        enabled_handlers = []
        if self.telegram_handler.enabled:
            enabled_handlers.append("Telegram")
        return enabled_handlers

    def send_notification(self, message):
        if self.telegram_handler.enabled:
            self.telegram_handler.send(message)
