import Tkinter as tk
import ttk


class CmInchConverter(object):
    """Simple conversion between length in cm to inch and inch to cm"""

    def __init__(self):
        """Initialize"""
        self._root = None
        self.value = "0"
        self.result = "0"
        self.convert_to_inches = None

    def run(self):
        """Create and execute program"""
        self._gui_initialize()
        self._root.mainloop()

    def _gui_initialize(self):
        """Initialize the GUI"""
        self._root = tk.Tk()
        self._root.title("inch/cm converter")

        self.convert_to_inches = tk.IntVar()
        self.value = tk.StringVar()
        self.result = tk.StringVar()
        self.convert_to_inches.set(1)
        self.value.set("0")
        self.result.set("0")

        mainframe = ttk.Frame(self._root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        defaults = {"padx": 2, "pady": 2, "sticky": tk.W}

        radio1 = tk.Radiobutton(mainframe,
                                text="cm to inches",
                                padx=2,
                                variable=self.convert_to_inches,
                                value=1)
        radio1.grid(column=0, row=2, columnspan=2, **defaults)
        radio2 = tk.Radiobutton(mainframe,
                                text="inches to cm",
                                padx=2,
                                variable=self.convert_to_inches,
                                value=2)
        radio2.grid(column=0, row=3, columnspan=2, **defaults)

        ttk.Label(mainframe, text="Enter value:").grid(column=0, row=1,
                                                       **defaults)
        entry1 = ttk.Entry(mainframe, width=20, textvariable=self.value)
        entry1.grid(column=1, row=1, **defaults)

        ttk.Label(mainframe, text="Result:").grid(column=0, row=4, **defaults)

        entry2 = tk.Entry(mainframe, width=20, state=tk.DISABLED,
                          textvariable=self.result,
                          disabledbackground="White Smoke",
                          disabledforeground="Midnight Blue")
        entry2.grid(column=1, row=4, **defaults)
        ttk.Button(mainframe, text="Calculate",
                   command=self.calculate).grid(column=3, row=5, **defaults)


    def calculate(self):
        """Perform calculation"""
        action = {1: self._inch_calculate,
                  2: self._cm_calculate}
        try:
            val = int(self.value.get())
        except ValueError:
            val = self.value.get()

        result = action[self.convert_to_inches.get()](val)
        self.result.set(result)

    def _cm_calculate(self, val):
        """Calculate cm value from given val in inch"""
        try:
            return "%.4f" % val/0.3937
        except TypeError:
            return "Err"

    def _inch_calculate(self, val):
        """Calculate inch value from given val in cm"""
        try:
            return "%.4f" % val * 0.3937
        except TypeError:
            return "Err"


def main():
    """Main function"""
    conv = CmInchConverter()
    conv.run()


if __name__ == '__main__':
    main()
