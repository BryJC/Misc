class Decoder(object):
    
    def __init__(self):
        pass

    def scanner(self, text):

        x = list(text)
        y = []
        z = []
        for i in x:
            try:
                int(i)
            except ValueError:
                y.append(i)
        z_string = ''.join(y)
        return z_string

decodes = Decoder()
