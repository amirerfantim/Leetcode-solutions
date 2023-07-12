class Solution122 {
    public int maxProfit(int[] prices) {
        int max_profit = 0;
        for (int i = 0; i < prices.length - 1; i++){
            if (prices[i+1] > prices[i]){
                max_profit += prices[i+1] - prices[i];
            }
        }
        return max_profit;
    }
}