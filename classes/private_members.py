# When we want to make an attribute private we prefix with double underscore
# this way "tags" is now "__tags"

class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
print(cloud.__dict__)  # with this we can see the renaming of the attribute
print(cloud._TagCloud__tags)  # "__tags" is not really private
# anyway we call it private because is harder to access from outside
# but in Python we don't have actually private attributes
