from typing import List, Dict
from html.parser import HTMLParser


class NDBHtmlParser(HTMLParser):
    def error(self, message):
        pass

    def __init__(self):
        HTMLParser.__init__(self)
        self.__tree = None
        self.__elementsStack = []

    def analyze(self, data: str) -> None:
        self.__tree = None
        self.__elementsStack = []
        self.feed(data)
        self.close()

        if self.__elementsStack:
            self.__tree = self.__elementsStack.pop()

    def get_tree(self) -> 'Tag':
        return self.__tree

    def find_one(self, name: str =None, after: 'Tag'=None, before: 'Tag'=None, params: dict=None) -> 'Tag':
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

    def find_all(self, name: str=None, after: 'Tag'=None, before: 'Tag'=None, params: dict=None) -> List['Tag']:
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

    def handle_starttag(self, tag, attrs) -> None:
        to_add = Tag(tag, attrs=dict(attrs))
        self.__elementsStack.append(to_add)

    def handle_endtag(self, tag) -> None:
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

    def handle_data(self, data) -> None:
        #   TO DO: rest unicode char to null
        data = data.translate({ord('\xc5'): '', ord('\xa0'): '', ord('\n'): '',
                               ord('\t'): '', ord('\r'): '', ord('\f'): ''})
        data = data.strip()
        try:
            self.__elementsStack[-1].data += data
        except IndexError:
            pass


class Tag(object):
    def __init__(self, name: str, data: str='', attrs: dict=None, parent: 'Tag'=None, next_sib: 'Tag'=None,
                 prev_sib: 'Tag'=None, children: List['Tag']=None):
        self.name = name    # type: str
        self.data = data    # type: str
        self.attrs = [] if attrs is None else attrs     # type: Dict[str]
        self.parent = parent    # type: 'Tag'
        self.next_sib = next_sib    # type: 'Tag'
        self.prev_sib = prev_sib    # type: 'Tag'
        self.children = [] if children is None else children    # type: List['Tag']
        for child in self.children:
            child.parent = self

    def has_attr(self, params: dict) -> bool:
        if not params:
            return True

        for attr_key in self.attrs:
            for par_key in params:
                if par_key == attr_key and params[par_key] == self.attrs[attr_key]:
                    return True
        return False

    def add_child(self, child: 'Tag') -> None:
        child.parent = self
        if self.children:
            self.children[-1].next_sib, child.prev_sib = child, self.children[-1]
        self.children.append(child)

    def prev(self) -> 'Tag':
        if self.prev_sib:
            return self.prev_sib
        elif self.parent:
            return self.parent
        else:
            raise StopIteration

    def __next__(self) -> 'Tag':
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

    def next_data(self) -> str:
        next_tag = self.next()
        if next_tag:
            return next_tag.data
        return ''

    def prev_data(self) -> str:
        next_tag = self.prev()
        if next_tag:
            return next_tag.data
        return ''

    def __repr__(self) -> str:
        return self.__str__()

    def __iter__(self):
        return self

    def __str__(self) -> str:
        result = "<" + str(self.name)

        for key in self.attrs:
            result += " " + str(key) + "=\"" + str(self.attrs[key]) + "\""
        result += ">" + str(self.data)

        for child in self.children:
            result += str(child)

        result += "</" + str(self.name) + ">"

        return result
