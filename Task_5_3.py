from Task_5_1 import UserInputValidator

instance_one = UserInputValidator()
instance_two = UserInputValidator()

test_one = ["Hello","World","!","1","-2","0"]
test_two = ["3.4","2","1","0","-1"]

result_one = instance_one.validate_positive_integers(test_one)
print(result_one)

result_two = instance_two.validate_positive_integers(test_two)
print(result_two)