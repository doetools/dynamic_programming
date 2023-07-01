from typing import List


def max_rob(nums: List[int]) -> int:
    """Maximize robbery gains without alerting the police.

    Examples:
        >>> nums = [1,2,3,1]
        >>> max_rob[nums]
        4
        >>> nums = [2,7,9,3,1]
        12
        >>> nums = [0]
        0

    Args:
        nums: A list indicating the money stashed in each house.

    Returns:
        A number indicating the maximum amount of robbery.
    """

    if not nums:
        return 0

    # two states (possible actions) at each house
    # rob or not rob, befinits of which
    # are depdent on previous states
    not_rob = 0
    rob = nums[0]

    N = len(nums)

    for i in range(1, N):
        # at current step i, looking back at step i-1:
        # if robbing, then only one option, which is the previous
        # house was not robber

        # if not robbing, then there are two options, first being the
        # previous house not robbed, and second being the previous house
        # robbed
        not_rob, rob = max(rob, not_rob), not_rob + nums[i]

    return max(not_rob, rob)


if __name__ == "__main__":
    inputs = [[1, 2, 3, 1], [2, 7, 9, 3, 1], []]
    expected = [4, 12, 0]
    input_zip = zip(inputs, expected)

    for i, e in input_zip:
        print(f"max gain for input {i} with expected value of {e}: {max_rob(i)}")
