from Products.Five import BrowserView


class TestView(BrowserView):
    def edit_title(self):
        self.context.setTitle(self.request.form['title'])
        self.context.reindexObject(idxs=['Title'])
        self.request.response.redirect(
            self.context.absolute_url() + '/htmx_view')
