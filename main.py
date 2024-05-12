from gui import *


def main():
    window = Tk()
    window.title('Project 1')
    window.geometry('400x380')
    window.resizable(False, False)

    Gui(window)
    window.mainloop()


if __name__ == '__main__':
    main()
