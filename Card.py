class Card:
    tapped = False

    def is_tapped(self):
        return self.tapped

    def tap(self):
        self.tapped = True

    def untap(self):
        self.tapped = False

    def toogle_tap(self):
        if self.is_tapped():
            self.untap()
        elif not self.is_tapped():
            self.tap()
