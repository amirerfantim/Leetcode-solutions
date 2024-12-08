class Solution26 {
    public int removeDuplicates(int[] nums) {
        int org_index = 0;
        int unique_index = 1;

        for (org_index = 0 ; org_index < nums.length - 1; org_index++){
            if (nums[org_index] != nums[org_index + 1]){
                nums[unique_index] = nums[org_index + 1];
                unique_index += 1;


            }

        }
        return unique_index;
    }
}