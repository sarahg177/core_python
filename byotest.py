def number_of_evens(numbers):
    return 0

def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format (expected, actual)
    
def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b)
    
test_are_equal(number_of_evens([1,2,3,4,5]),2)