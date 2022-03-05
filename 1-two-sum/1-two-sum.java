class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> indexMap = new HashMap<>();
        for(int i=0; i < nums.length; i++) {
            Integer key = (Integer)target - nums[i];
            if(indexMap.containsKey(key)) {
                return new int[] {indexMap.get(key), i};
            }
            indexMap.put((Integer)nums[i], i);
        }
        return null;
    }
}