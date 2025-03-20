import toga
import psycopg2


class addSession(toga.Box):

    def __init__(self, on_press, cursor, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_press = on_press

        historyButton = toga.Button(
            text="See history",
            on_press = self.on_press
        )

        validateButton = toga.Button(
            text="Validate",
            on_press = self.validate
        )

        self.reps_input = toga.TextInput()
        
        self.add(historyButton)
        self.add(self.reps_input)
        self.add(validateButton)

    def validate(self,widget):
        
        print(self.reps_input.value)