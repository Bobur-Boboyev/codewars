def missing(nums, s):
    nums = sorted(nums)
    s = s.replace(' ', '')
    
    st = ''
    
    for i in nums:
        if i >= len(s):
            return 'No mission today'
        else:
            st += s[i].lower()
    
    return st