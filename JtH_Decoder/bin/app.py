import web
from jthdecoder import *

urls = (
  '/decoder', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class Index:

    def GET(self):
        return render.decoder_form()
                   
    def POST(self):
        form = web.input(decode="""Nope!""")
        x = """""".join(form.decode)
        true_text = decodes.scanner(x)
        return render.index(true_text = true_text)

if __name__ == "__main__":
    app.run()
