class Solution4 {
    public static int removeDuplicates(int[] nums) {
        int unique_index = 2;

        for (int org_index = 0 ; org_index < nums.length - 2 ; org_index++){
            if (nums[org_index] != nums[unique_index]){
                nums[unique_index] = nums[org_index];
                unique_index++;
            }
        }
        return unique_index;
    }


}