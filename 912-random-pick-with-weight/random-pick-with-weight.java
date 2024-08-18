class Solution {

     private int[] prefixSum;

    public Solution(int[] w) {
        int length = w.length;
        this.prefixSum = new int[length + 1];
        this.prefixSum[0] = 0;
        for (int i = 1; i < length + 1; i++) {
            this.prefixSum[i] = this.prefixSum[i - 1] + w[i - 1];
        }
    }

    public int pickIndex() {
        int l = this.prefixSum.length;
        int low = 1;
        int high = this.prefixSum[l - 1];
        Random random = new Random();
        int randomIndex = random.nextInt(high - low + 1) + 1;
        return leftBound(low, l - 1, randomIndex) - 1;
    }

    private int leftBound(int low, int high, int target) {
        System.out.println(this.prefixSum);
        while (low < high) {
            int mid = (high - low) / 2 + low;
            if (this.prefixSum[mid] == target) {
                high = mid;
            } else if (this.prefixSum[mid] < target) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.pickIndex();
 */