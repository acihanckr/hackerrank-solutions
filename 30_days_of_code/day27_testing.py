import random


#start


class TestDataEmptyArray:
    
    @staticmethod
    def get_array():
        return list()


class TestDataUniqueValues:
    
    @classmethod
    def get_array(cls):
        cls.minimum = random.randint(2, 100)
        arr = [cls.minimum*rand for rand in random.sample(range(2,100),random.randint(5,20))]
        arr.insert(random.randint(0,len(arr)),cls.minimum)
        return arr
    
    @classmethod
    def get_expected_result(cls):
        return cls.minimum


class TestDataExactlyTwoDifferentMinimums:
    
    @classmethod
    def get_array(cls):
        cls.minimum = random.randint(2, 100)
        arr = [cls.minimum*rand for rand in random.sample(range(2,100),random.randint(0,20))]
        arr.append(cls.mininum)
        arr += [cls.mininum*rand for rand in random.sample(range(2,100),random.randint(0,20))]
        arr.append(cls.mininum)
        arr += [cls.mininum*rand for rand in random.sample(range(2,100),random.randint(0,20))]
        return arr 
    
    @classmethod
    def get_expected_result(cls):
        return cls.mininum


#end

def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False

def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")
