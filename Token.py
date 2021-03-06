from Constants import Token_type

class Token :
    def __init__(self, token_type: Token_type, value) :
        self.token_type = token_type
        if token_type == Token_type.INTEGER:
            self.value = int(value)
        else:
            self.value = value

    def __str__(self) :
        return 'Token("{type}","{value}")'.format(type=repr(self.token_type), value=self.value)

    def __repr__(self):
        return self.__str__()
