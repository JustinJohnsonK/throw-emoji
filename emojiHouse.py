class emojiHouse:
    """
    Class contain all emojies,
    divided amoung various groups.
    """
    def __init__(self, emotion):
        self.emotion = emotion

    def port(self):
        if(self.emotion == 'veryHappy'):
            emojies = self.veryHappyHome()

        elif(self.emotion == 'happy'):
            emojies = self.happyHome()

        elif(self.emotion == 'nothing'):
            emojies = self.silentHome()

        elif(self.emotion == 'sad'):
            emojies = self.sadHome()

        elif(self.emotion == 'verySad'):
            emojies = self.heartbrokenHome()

        return emojies


# unicodes u'\U0001f600' to u'\U0001f644'
    def veryHappyHome(self):
        home = [u'\U0001f604', u'\U0001f605', u'\U0001f602', u'\U0001f606', u'\U0001f618', u'\U0001f642']
        return home

    def happyHome(self):
        home = [u'\U0001f600', u'\U0001f601', u'\U0001f603', u'\U0001f607', u'\U0001f609', u'\U0001f617', 
        u'\U0001f619', u'\U0001f638']
        return home

    def silentHome(self):
        home = [u'\U0001f610', u'\U0001f611', u'\U0001f615', u'\U0001f632', u'\U0001f633', u'\U0001f634', 
        u'\U0001f636', u'\U0001f637', u'\U0001f644']
        return home

    def sadHome(self):
        home = [u'\U0001f612', u'\U0001f613', u'\U0001f614', u'\U0001f621', u'\U0001f622', u'\U0001f623',
        u'\U0001f625', u'\U0001f626', u'\U0001f627', u'\U0001f628', u'\U0001f641']
        return home

    def heartbrokenHome(self):
        home = [u'\U0001f608', u'\U0001f616', u'\U0001f620', u'\U0001f624', u'\U0001f629', u'\U0001f630', 
        u'\U0001f631', u'\U0001f635']
        return home