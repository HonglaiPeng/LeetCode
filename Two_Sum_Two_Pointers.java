class Solution {
    public int[] twoSum(int[] nums, int target) {
        // two pointers
        // create new array and copy the original array, then sort the copy array
        
        int[] res = new int[2];
        int[] CopyOfNums = Arrays.copyOf(nums, nums.length);
        Arrays.sort(CopyOfNums);
        
        // create two pointers, start pointer and end pointer
        int start = 0, end = nums.length - 1;
        
        // logic:
        // if nums[start] + nums[end] > target, we need move end pointer
        // if nums[start] + nums[end] < target, we need move start pointer
        
        // because we use the copy array to search, so we need store the num not the index.
        int num1 = 0;
        int num2 = 0;
        int sum = 0;
        while(start < end){
            sum = CopyOfNums[start] + CopyOfNums[end];
            if(sum > target){
                end--;
            }else if(sum < target){
                start++;
            }else{
                num1 = CopyOfNums[start];
                num2 = CopyOfNums[end];
                break;
            }
        }
        
        // Now, we need use num1 and num2 to get the index
        // cases:
        // 1. num1 != num2
        // 2. num1 == num2
        
        if(num1 == num2){
            for(int i = 0; i < nums.length; i++){
                if(nums[i] == num1){
                    res[0] = i;
                }
            }
            for(int i = 0; i < nums.length; i++){
                if(nums[i] == num2 && i != res[0]){
                    res[1] = i;
                }
            }
        }else{
            for(int i = 0; i < nums.length; i++){
                if(nums[i] == num1){
                    res[0] = i;
                }
                if(nums[i] == num2){
                    res[1] = i;
                }
            }
        }
        
        
        return res;
    }
}