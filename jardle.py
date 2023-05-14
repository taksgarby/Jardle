class Jardle:

    MAX_ATTEMPTS = 6
    WORD_LENGTH = 4

    def __init__(self, secret:str):
        self.secret: str = secret
        self.attempts = []
        pass
        