class CartIntegrityError(Exception):

    def __init__(self, mssg):
        self.mssg = mssg
