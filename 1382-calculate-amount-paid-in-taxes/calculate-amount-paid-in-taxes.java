class Solution {
    public double calculateTax(int[][] brackets, int income) {
        double totalTax = 0.0d;
        int previous = 0;
        for (int[] bracket : brackets){
            if (income <= 0){
                break;
            }
            int upper = bracket[0];
            int percentage = bracket[1];

            int diff = Math.min(upper - previous, income);

            totalTax += (double) diff * ((double) percentage / 100);
            income -= diff;
            previous = upper;

        } 

        return totalTax;

        
    }
}