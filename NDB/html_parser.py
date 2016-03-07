from html.parser import HTMLParser


class NDBHtmlParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__tree = None
        self.__elementsStack = []

    def analyze(self, data):
        self.__tree = None
        self.__elementsStack = []
        self.feed(data)
        self.close()

        if self.__elementsStack:
            self.__tree = self.__elementsStack.pop()

    def get_tree(self):
        return self.__tree

    def find_one(self, name=None, after=None, before=None, params=None):
        if after and not isinstance(after, Tag):
            raise TypeError("After is not instance of Tag class")
        if before and not isinstance(before, Tag):
            raise TypeError("Before is not instance of Tag class")
        if params and not isinstance(params, dict):
            raise TypeError("Params is not instance of dictionary class")

        root = self.__tree if after is None else after
        next_tag = Tag(name="root", next_sib=root)
        while True:
            try:
                next_tag = next(next_tag)

                if before and before == next_tag:
                    raise StopIteration
                elif name and next_tag.name != name:
                    continue
                elif next_tag.has_attr(params):
                    return next_tag

            except StopIteration:
                return None

    def find_all(self, name=None, after=None, before=None, params=None):
        if after and not isinstance(after, Tag):
            raise TypeError("After is not instance of Tag class")
        if before and not isinstance(before, Tag):
            raise TypeError("Before is not instance of Tag class")
        if params and not isinstance(params, dict):
            raise TypeError("Params is not instance of dictionary class")

        root = self.__tree if after is None else after
        next_tag = Tag(name="root", next_sib=root)
        result = []
        while True:
            try:
                next_tag = next(next_tag)

                if before == next_tag:
                    raise StopIteration
                elif name and next_tag.name != name:
                    continue
                elif next_tag.has_attr(params):
                    result.append(next_tag)

            except StopIteration:
                return result

    def handle_starttag(self, tag, attrs):
        to_add = Tag(tag, attrs=dict(attrs))
        self.__elementsStack.append(to_add)

    def handle_endtag(self, tag):
        try:
            poped = self.__elementsStack.pop()
            if not self.__elementsStack:
                if not self.__tree:
                    self.__tree = poped
                else:
                    self.__tree.add_child(poped)
            else:
                self.__elementsStack[-1].add_child(poped)
        except IndexError:
            pass

    def handle_data(self, data):
        #   TO DO: rest unicode char to null
        data = data.translate({ord('\xa0'): '', ord('\n'): '', ord('\t'): '', ord('\r'): '', ord('\f'): ''})
        data = data.strip()
        try:
            self.__elementsStack[-1].data += data
        except IndexError:
            pass


class Tag(object):
    def __init__(self, name, data='', attrs=None, parent=None, next_sib=None, prev_sib=None, children=None):
        self.name = name
        self.data = data
        self.attrs = [] if attrs is None else attrs
        self.parent = parent
        self.next_sib = next_sib
        self.prev_sib = prev_sib
        self.children = [] if children is None else children
        for child in self.children:
            child.parent = self

    def has_attr(self, params):
        if not params:
            return True

        for attr_key in self.attrs:
            for par_key in params:
                if par_key == attr_key and params[par_key] == self.attrs[attr_key]:
                    return True
        return False

    def add_child(self, child):
        child.parent = self
        if self.children:
            self.children[-1].next_sib, child.prev_sib = child, self.children[-1]
        self.children.append(child)

    def prev(self):
        if self.prev_sib:
            return self.prev_sib
        elif self.parent:
            return self.parent
        else:
            raise StopIteration

    def __next__(self):
        if self.children:
            return self.children[0]
        elif self.next_sib:
            return self.next_sib

        parent = self.parent
        while parent:
            if parent.next_sib:
                return parent.next_sib
            parent = parent.parent
        else:
            raise StopIteration

    next = __next__

    def next_data(self):
        next_tag = self.next()
        if next_tag:
            return next_tag.data
        return ''

    def prev_data(self):
        next_tag = self.prev()
        if next_tag:
            return next_tag.data
        return ''

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        result = "<" + str(self.name)

        for key in self.attrs:
            result += " " + str(key) + "=\"" + str(self.attrs[key]) + "\""
        result += ">" + str(self.data)

        for child in self.children:
            result += str(child)

        result += "</" + str(self.name) + ">"

        return result
