from abc import ABC, abstractmethod


class UTIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UTIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UTIControl):
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()

# def draw(controls):
#     controls.draw()


ddl = DropDownList()
print(isinstance(ddl, UTIControl))

# draw(ddl)
textBox = TextBox()
# draw(textBox)

draw([ddl, textBox])
