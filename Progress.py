import time


class Progress:
    def __init__(self, title='', refresh_rate=1.0):
        self.title = title
        self.previous_progress = ''
        self.refresh_rate = refresh_rate
        self.last_refresh_time = time.time()

    def print_progress(self, progress):
        if time.time() - self.last_refresh_time < self.refresh_rate:
            return

        progress = self.title + str(progress)
        length_diff = len(self.previous_progress) - len(progress)
        padding = ' ' * length_diff if length_diff > 0 else ''
        print('\r' + progress + padding, end='', flush=True)
        self.previous_progress = progress
        self.last_refresh_time = time.time()
