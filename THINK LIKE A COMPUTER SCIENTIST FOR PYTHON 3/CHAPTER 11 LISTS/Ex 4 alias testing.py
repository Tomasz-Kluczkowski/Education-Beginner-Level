this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]
print("Test 1: {0}".format(this is that)) # should be false
that = this
print("Test 2: {0}".format(this is that)) # should be true

