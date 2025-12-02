class Dial:
    def __init__(self, value=0):
        self.value = value % 100
        self.zero_passes = 0

    def turn_left(self, clicks=1):
        old_position = self.value
        new_position = old_position - clicks

        if new_position <= 0 and old_position > 0:
            passes = 1 + (-new_position) // 100
        elif new_position <= 0:
            passes = (-new_position - (100 - old_position)) // 100 + 1
        else:
            passes = 0

        self.value = new_position % 100
        self.zero_passes += passes

    def turn_right(self, clicks=1):
        old_position = self.value
        new_position = old_position + clicks

        passes = (new_position) // 100 - (old_position) // 100

        self.value = new_position % 100
        self.zero_passes += passes


def main():
    with open("input.txt") as f:
        dial = Dial(50)
        lines = f.readlines()
        for line in lines:
            current_line = line.strip()
            clicks = int(current_line[1:])

            if current_line.startswith("L"):
                dial.turn_left(clicks)
            elif current_line.startswith("R"):
                dial.turn_right(clicks)

        print(dial.zero_passes)


if __name__ == "__main__":
    main()
