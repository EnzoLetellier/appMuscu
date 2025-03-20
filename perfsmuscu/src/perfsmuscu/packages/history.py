import toga

class history(toga.Box):
    def __init__(self, on_press, cursor, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_press = on_press

        label = toga.Label('This Is history')

        addButton = toga.Button (
            text="add session",
            on_press = self.on_press
        )

        self.add(label)
        self.add(addButton)