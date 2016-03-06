from html.parser import HTMLParser


class NDBHtmlParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.__htmlObject = {}
        self.__elementsStack = []

    def analyze(self, data):
        self.feed(data)
        self.close()

    def get_element_by_attr(self, tag, attr, val):
        try:
            for ele in self.__htmlObject[tag]:
                for ele_attr in ele['attrs']:
                    if ele_attr[0] == attr and ele_attr[1] == val:
                        return ele
        except AttributeError:
            return None

    def get_data_by_attr(self, tag, attr, val):
        try:
            #print(str(self.__htmlObject))
            for ele in self.__htmlObject[tag]:
                #print("ele: " + str(ele))
                for ele_attr in ele['attrs']:
                    #print("ele_attr: " + str(ele_attr))
                    if ele_attr[0] == attr and ele_attr[1] == val:
                        return ele['data']
        except AttributeError:
            return None

    def handle_starttag(self, tag, attrs):
        #print("Start tag:", tag)
        #for attr in attrs:
            #print("     attr:", attr)
        to_add = {
            'tag': tag,
            'attrs': attrs,
            'data': ''
        }
        self.__elementsStack.append(to_add)

    def handle_endtag(self, tag):
        #print("End tag  :", tag)
        if not tag in self.__htmlObject:
            self.__htmlObject[tag] = []

        poped = self.__elementsStack.pop()
        #print("poped: " + str(poped))
        self.__htmlObject[tag].append(poped)
        #print("obj: " + str(self.__htmlObject[tag]))

    def handle_data(self, data):
        data = data.strip()
        #print("Data: ", data)
        try:
            if data:
                self.__elementsStack[-1]['data'] += data
        except IndexError:
            pass
