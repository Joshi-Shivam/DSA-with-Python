class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        max_val = 0
        if need1 > need2:
            max_val = need1
        elif need1 == need2:
            max_val = need1
        else:
            max_val = need2
        min_val = 0
        if need1 < need2:
            min_val = need1
        elif need1 == need2:
            min_val = need1
        else:
            min_val = need2
        cost_separate = (need1 * cost1) + (need2 * cost2)
        cost_max_combos = max_val * costBoth

        cost_overlap = (min_val * costBoth) + ((need1 - min_val) * cost1) + ((need2 - min_val) * cost2)

        # Your final comparison expanded to check all three
        if cost_separate <= cost_max_combos and cost_separate <= cost_overlap:
            return cost_separate
        elif cost_max_combos <= cost_separate and cost_max_combos <= cost_overlap:
            return cost_max_combos
        else:
            return cost_overlap