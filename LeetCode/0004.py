class Solution:
    def calMid(self, nums): # sorted arrary: nums:
        mlength = len(nums)
        mid = mlength >> 1
        if mlength%2==0:
            return (nums[mid]+nums[mid-1])/2.0
        else:
            return nums[mid]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        if m == 0:
            return self.calMid(nums2)
        elif n == 0:
            return self.calMid(nums1)

        nums3 = [0] * (m+n)
        m_index, n_index = 0, 0
        for p_index in range(m+n):
            if nums1[m_index] >= nums2[n_index]:
                nums3[p_index] = nums2[n_index]
                n_index += 1
            else:
                nums3[p_index] = nums1[m_index]
                m_index += 1
            
            if m_index == m or n_index == n:
                break

        if m_index == m:
            for j in range(n_index, n):
                nums3[m+j] = nums2[j]
        elif n_index == n:
            for j in range(m_index, m):
                nums3[n+j] = nums1[j]
        
        # print(nums3)
        return self.calMid(nums3)

            
