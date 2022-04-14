from tkinter import Tk, Canvas, Frame, BOTH


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Castl")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)

        # основа замка.
        canvas.create_rectangle(
            10, 150, 320, 400,
            outline="black",
            width=2
        )

        # текстура основного здания
        x = 200
        for i in range(0, 5):
            canvas.create_line(
                (10, x),
                (320, x)
            )
            x += 50

        # основа башни.
        canvas.create_rectangle(
            320, 100, 420, 400,
            outline="black",
            width=2
        )

        # крыша башни
        canvas.create_polygon(
            (300, 100),
            (370, 40),
            (440, 100),
            fill="blue",
            outline="black"
        )

        # окно башни
        canvas.create_rectangle(
            350, 140, 390, 200,
            fill="teal",
            outline="blue"
        )

        # трава
        y = 10
        for i in range(0, 50):
            canvas.create_line(
                (y, 450),
                (y + 10, 410),
                fill="green"
            )
            y += 10

        # гербы
        canvas.create_polygon(
            (240, 150),
            (290, 150),
            (290, 290),
            (265, 315),
            (240, 290),
            fill="red"
        )
        canvas.create_polygon(
            (40, 150),
            (90, 150),
            (90, 290),
            (65, 315),
            (40, 290),
            fill="red"
        )

        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = Example()
    root.geometry("700x500")
    root.mainloop()


main()
