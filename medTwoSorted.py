def findMedianSortedArrays(nums1, nums2):
    mergedList = []
    ai = int(0)
    bi = int(0)
    alen = len(nums1)
    blen = len(nums2)
    while ai < alen and bi < blen:
        if nums1[ai] < nums2[bi]:
            mergedList.append(nums1[ai])
            ai += 1
        else :
            mergedList.append(nums2[bi])
            bi += 1
    if ai < alen:
        while ai < alen:
            mergedList.append(nums1[ai])
            ai += 1
    if bi < blen:
        while bi < blen:
            mergedList.append(nums2[bi])
            bi += 1
    mLen = len(mergedList)
    if mLen % 2 == 0:
        return (mergedList[mLen // 2] + mergedList[(mLen // 2)-1]) / 2
    else:
        return mergedList[mLen // 2]