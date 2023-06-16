# With this 2 examples you can see how easy it is to extend built-in classes
class Text(str):
    def duplicate(self):
        return self + self


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


text = Text("Python")
print(text.lower())
print(text.duplicate())
print("---------------------------------------------------------")

list = TrackableList()
list.append("1")
