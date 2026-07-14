class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        holder=s.split()
        holder.reverse()
        return " ".join(holder)