from django.apps import AppConfig


class ChatConfig(AppConfig):
    name = 'dual_rocks.chat'

    def ready(self):
        import dual_rocks.chat.signals  # noqa: F401
