
class TextBox:
    def draw(self):
        print("TextBox")


class DropDownList:
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()

# def draw(controls):
#     controls.draw()


ddl = DropDownList()

# draw(ddl)
textBox = TextBox()
# draw(textBox)

draw([ddl, textBox])
