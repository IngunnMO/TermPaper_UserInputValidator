class UserInputValidator:

    def validate_positive_integers(self,input):
        result = []
        for item in input:
            if item.isdigit() and int(item) != 0:
                result.append(int(item))
            else:
                continue
        self.__display_message()
        return result

    def __display_message(self):
        print("The below list has been successfully validated.")