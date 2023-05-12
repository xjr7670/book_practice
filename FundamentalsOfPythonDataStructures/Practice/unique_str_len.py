# L1 = [1, 3, 5, 6, 9, 0, 8, 7]
# print('奇数: ' + ' '.join([str(x) for x in L1 if x % 2 == 1]))
# print('偶数：' + ' '.join([str(x) for x in L1 if x % 2 == 0]))


def get_longest_substr(s):

    unique_set = set()
    max_ = -1
    start = 0
    max_pair = [0, 0]  # [长度, 开始位置]
    for idx, c in enumerate(s):
        if c not in unique_set:
            unique_set.add(c)
        else:
            cur_len = idx - start
            pair = [cur_len, start]
            start = idx-1
            if cur_len > max_:
                max_pair = pair
                max_ = cur_len

    else:
        return s[max_pair[1]: max_pair[1] + max_pair[0]]


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    tmp_set = dict()
    start = 0
    longest = 0
    for idx, c in enumerate(s, start=1):
        if c in tmp_set:
            start = max(tmp_set[c], start)
        longest = max(longest, idx-start)
        tmp_set[c] = idx
    return longest


def length_of_longest_substring(s):
    unique_set = set()
    max_ = -1
    start = 0
    for idx, c in enumerate(s, start=1):
        if c not in unique_set:
            unique_set.add(c)
        else:
            start += 1
        cur_len = idx - start
        if cur_len > max_:
            max_ = cur_len
    return max_


if __name__ == '__main__':

    s1 = 'abcdbefgf'
    s2 = 'pwwkew'
    s3 = 'dvcdf'
    print(length_of_longest_substring(s3))

