from Products.Five import BrowserView


class TestView(BrowserView):
    def replace_button(self):
        return "<p>Replaced</p>"
