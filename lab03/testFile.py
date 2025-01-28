from lab03 import integerDivision
from lab03 import collectEvenInts
from lab03 import countVowels
from lab03 import reverseString
from lab03 import removeSubString

def test_integerDivision():
    assert integerDivision(27,4) == 6
    assert integerDivision(4,6) == 0
    assert integerDivision(8,4) == 2
    assert integerDivision(9,4) == 2

def test_collectEvenInts():
    assert collectEvenInts([1,2,3,4,5]) == [2,4]
    assert collectEvenInts([-1,-2,-3,-4,-5]) == [-2, -4]
    assert collectEvenInts([]) == []
    assert collectEvenInts([0, 0, 2, 2, 4, -1]) == [0, 0, 2, 2, 4]

def test_countVowels():
    assert countVowels("This Is A String") == 4    
    assert countVowels("Jason") == 2
    assert countVowels("") == 0
    assert countVowels("aeiou556") == 5  
    assert countVowels("556") == 0

def test_reverseString():
    d1 = reverseString("Jason")
    d2 = reverseString("Jason12345")
    d3 = reverseString("jAsOn12")
    d4 = reverseString("aJo1Lp3as")
    assert d1 == "nosaJ"
    assert d2 == "54321nosaJ"
    assert d3 == "21nOsAj"
    assert d4 == "sa3pL1oJa"

def test_removeSubString():
    assert removeSubString("Lolololol", "lol") == "Loo"
    assert removeSubString("jajajaJA", "ja") == "JA"
    assert removeSubString("12341", "23") == "141"
    assert removeSubString("12341jaja", "23ja") == "12341jaja"
    assert removeSubString("asdj123K123bg", "123K") == "asdj123bg"