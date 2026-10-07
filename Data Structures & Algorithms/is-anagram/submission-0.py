class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        trackS = {}
        trackT = {}

        for l in range(len(t)):
            trackS[s[l]] = 1 + trackS.get(s[l], 0)
            trackT[t[l]] = 1 + trackT.get(t[l], 0)

        return trackS == trackT


