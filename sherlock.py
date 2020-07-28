
"""
Given a string, find the number of pairs of substrings of the string that are anagrams of each other.
must return an integer that represents the number of anagrammatic pairs of substrings in s.
"""
def sherlockAndAnagrams(s):
    d = {}
    ans = 0
    for i in range(len(s)):
        add = 0
        mul = 1
        for j in range(i,len(s)):
            add += ord(s[j])
            mul *= ord(s[j])
            check = (add, mul)
            ex = d.get(check, 0)
            ans += ex
            d[check] = ex + 1
    return ans

if __name__ == '__main__':
    print(sherlockAndAnagrams('abba'))
    print(sherlockAndAnagrams('abcd'))
    print(sherlockAndAnagrams('ifailuhkqq'))
    print(sherlockAndAnagrams('kkkk'))
    print(sherlockAndAnagrams('cdcd'))
