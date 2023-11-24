import paralleldots

class API:
    def __init__(self):
        paralleldots.set_api_key('KSrHlbfRTIAGDSC01wRHenL2hfndFVfbeqAdhxSUhsw')

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response

    def ner(self,text):
        response = paralleldots.ner(text)
        return response