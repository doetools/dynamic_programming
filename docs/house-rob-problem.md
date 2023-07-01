## Problem

Given a list of integers indicating money stashes at each house, find the maximum amount of money one can rob without being caught by the police. The rule is that if two adjacent houses are robbed, the police will be alerted.

For example, given a input of [1,2,3,1], the robbery strategy to maximize gains would be choosing houses 0 and 2 (0 indexed), which leads to a total of 1 + 3 = 4. Similarly, for a input of [2,7,9,3,1], the following houses would be picked: 0, 2, 4, leading to a total of 2 + 9 + 1 = 12.

## Analysis

At each house, the robber has two options: rob or not rob. However, the choice at current house `i` is directly dependent on the immediately prior one `i-1`. Of course, one can argue it is also implicitly dependently on choices made at `i-2`, `i-3`.... This case is foundamentally different from the probem of [finding longest increasing sublist](" "), which needs to explicitly review **all** the past decisions. The reason is because the states at `i-1` is already optimized (the past has no chance to be better).

To think through this methodically, we only need to track two states: gain associated with rob action (`s1`), and gain associated with not-rob action (`s2`). It may sound weird that how possible a robber that does not rob can have gains. Remember, here we are talking about a **continuous** (or dynamic, whatever you want to call it) state. At `i=0`, `s2` is 0, for sure. However, take `i=1` as an example, `s2` could be 0, which means continuing not robbing, or, `s1`, which means the robber chose to rob at previous house but not the current.

To make the decision at each house optimal, the robber has to be clever about how to not rob -- following the previous example, rob at last house and not current one, or, not robbing both (the robber has a option to not rob!). However, when the robber chooses to rob, there is only one possible scenario, that is the robber did not rob the previous house (`i-1`). Now, lets get back to making optimal decision at house `i` regarding how to not rob. Comparing `s1_i-1` (the max gains if the robber did rob at last house) and `s2_i-1` (the max gains if the robber did not rob at last house), the rob would pick whichever larger!

The time and space complexity is O(N) and O(1).

## Function

::: dp.house_rob

Run above example using `python -m dp.house_rob`.

## Reference

Ref: https://leetcode.com/problems/house-robber/
