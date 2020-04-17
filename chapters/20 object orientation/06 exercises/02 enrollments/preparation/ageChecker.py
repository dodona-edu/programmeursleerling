class AgeChecker(OutputProcessor):

    """
    Checks whether the regular date that corresponds to the given rollover date.
    """

    def __init__(self, day, month, year):


        # call initialization method of base class
        super().__init__()

        # rollover the number of days
        import datetime
        self.date = datetime.date(year, month, day)

    def evaluateReturn(self):

        # function that computes the correct answer
        import datetime
        today = datetime.date.today()
        years = today.year - self.date.year
        if (today.month, today.day) < (self.date.month, self.date.day):
            years -= 1

        # compute the expected return value based on the current day
        self.setExpectedOutput(channel='return', output=years)

        super().evaluateReturn()
