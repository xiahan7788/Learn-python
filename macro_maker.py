"""
Automatically make macros for FFBE on Memu
This program should go in the same folder as the scripts
    e.g. C:\\Microvirt\\MEmu\scripts
"""

from datetime import datetime

# These might need to be edited based on the resolution; these are for 1280x720
UNIT1 = (850, 500)
UNIT2 = (1000, 500)
UNIT3 = (1150, 500)
UNIT4 = (850, 200)
UNIT5 = (1000, 200)
UNIT6 = (1150, 200)

UNITS = [UNIT1, UNIT2, UNIT3, UNIT4, UNIT5, UNIT6]

class Macro:
    """
    This class represents a single macro file.

    Attributes:
        name (str): name of the macro
        file_name (str): name of the file
        current_time (int): keeps track of the timing for the macro
                            (NOT actual time)
            every second = 1000000
            millisecond = 1000
            frame = 16666
        text (str): contents of the macro file to be written
        info_entry (str): text to be inserted into the info.ini file
    """

    def __init__(self, name):
        self.name = name
        time = datetime.now()
        self.file_name = time.strftime("%Y%m%d%H%M%S") + ".mir"
        self.info_entry = (
            "[" + time.strftime("%Y-%m-%d%%20%H%%3A%M%%3A%S") + "]\n"
            + "name=" + name + "\n"
            + "replayTime=0\n"
            + "replayCycles=1\n"
            + "replayAccelRates=1\n"
            + "replayInterval=0\n"
            )
        self.current_time = 100000
        self.text = ""

    def add_unit(self, unit_num, delay):
        """
        Add one press for the macro.

        Args:
            unit_num (int): number of the unit to be pressed
            delay (int): delay in frames
        """
        unit_coords = UNITS[unit_num - 1]
        self.text += str(self.current_time + (delay * 16666))
        self.current_time += delay * 16666
        self.text += "--VINPUT--MULTI:1:0:" \
                   + str(unit_coords[0]) + ":" + str(unit_coords[1]) + "\n"
        self.text += str(self.current_time + 20)
        self.current_time += 20
        self.text += "--VINPUT--MULTI:1:1:0:720\n"

    def write_macro(self):
        """
        Write the macro to the file.
        """
        file = open(self.file_name, "w")
        file.write(self.text
                   + str(self.current_time + 200000) + "--VINPUT--MOUSE:0:0")
        file.close()
        file = open("info.ini", "a")
        file.write("\n\n" + self.info_entry)
        file.close()

    def print_everything(self):
        """
        Print everything relevant about this object.
        """
        print(self.file_name + " (" + self.name + "):")
        print(self.text
              + str(self.current_time + 200000) + "--VINPUT--MOUSE:0:0")
        print("\nPaste to the info.ini file:")
        print(self.info_entry)

def main():
    """
    Lead the user through making the macro.
    """
    name = input("Name for macro: ")
    macro = Macro(name)
    repeats = 0
    while True:
        delay = "0"
        if repeats != 0:
            delay = input("Frame delay between units: ")
        if delay == "":
            break;
        # TODO: input checking (between 1 and 6 and not already used)
        unit_num = input("Unit number: ")
        if unit_num == "":
            break;
        macro.add_unit(int(unit_num), int(delay))
        repeats += 1
    macro.write_macro()


if __name__ == "__main__":
    main()
