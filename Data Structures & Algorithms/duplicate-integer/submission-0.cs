public class Solution {
    public bool hasDuplicate(int[] nums) {
        bool noDuplicate = false;
        HashSet<int> numHash = new HashSet<int>();
        foreach (int i in nums){
            noDuplicate = numHash.Add(i);
            if(!noDuplicate) 
            {
                return true;
            }
        }
        return false;
    }
}