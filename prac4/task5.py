class HTML:
    resultCode = []
    tab = ''

    def makeTab(self, tab):
        tab += '    '
        return tab

    def __init__(self):
        HTML.resultCode = []

    class body:

        def __enter__(self):
            HTML.resultCode.append("<body>")
            HTML.tab = HTML.makeTab(self, HTML.tab)

        def __exit__(self, *args, **kwargs):
            HTML.resultCode.append("</body>")

    class div:
        count = 0

        def __enter__(self):
            HTML.resultCode.append(HTML.tab + "<div>")
            HTML.tab = HTML.makeTab(self, HTML.tab)

        def __exit__(self, *args, **kwargs):
            self.count += 1
            for i in range(0, self.count):
                HTML.tab = HTML.tab[:-4]
            HTML.resultCode.append(HTML.tab + "</div>")


    def p(self, value):
        tag = HTML.tab + "<p>" + value + "</p>"
        HTML.resultCode.append(tag)

    def get_code(self):
        result = ''
        for item in HTML.resultCode:
            result += item
            result += '\n'

        return result


html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
        with html.div():
            html.p('Третья строка.')
    with html.div():
        html.p('sdfjfsjsjfjnf')


print(html.get_code())
