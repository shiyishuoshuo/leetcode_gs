class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        for card in sorted(hand):
            if card in count:
                for next_card in range(card, card + groupSize):
                    if count[next_card] == 0:
                        return False
                    count[next_card] -= 1
                    if count[next_card] == 0:
                        count.pop(next_card)
        
        return True
        