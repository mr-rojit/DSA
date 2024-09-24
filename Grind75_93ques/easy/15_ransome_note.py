"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

"""

def canConstruct(ransomNote, magazine):
    ransom_dict = {}
    mag_dict = {}

    for i in ransomNote:
        if i not in magazine:
            return False
        if i in ransom_dict:
            ransom_dict[i] +=1
        else:
            ransom_dict[i] = 1
    
    for i in magazine:

        if i in mag_dict:
            mag_dict[i] +=1
        else:
            mag_dict[i] = 1
    
    print(ransom_dict)
    print(mag_dict)


    for k,v in ransom_dict.items():
        if mag_dict[k] < v:
            return False
    return True


print(canConstruct("fihjjjjei", "hjibagacbhadfaefdjaeaebgi"))