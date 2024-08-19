class RandomizedSet {

    private Map<Integer, Integer> valToIndexMap;
    private List<Integer> numbers;

    private Random random;

     public RandomizedSet() {
        this.valToIndexMap = new HashMap<>();
        this.numbers = new ArrayList<>();
        this.random = new Random();
    }

    public boolean insert(int val) {
         if (this.valToIndexMap.containsKey(val)){
             return false;
         }
         this.valToIndexMap.put(val, numbers.size());
         numbers.add(val);
         return true;
    }

    public boolean remove(int val) {
         if(!this.valToIndexMap.containsKey(val)){
             return false;
         }
         int lastElement = this.numbers.get(this.numbers.size() - 1);
         int indexToRemove = this.valToIndexMap.get(val);
         this.valToIndexMap.put(lastElement, indexToRemove);
         this.numbers.set(indexToRemove, lastElement);
         this.numbers.remove(this.numbers.size() - 1);
         this.valToIndexMap.remove(val);
         return true;
    }

    public int getRandom() {
         int randomIndex = this.random.nextInt(this.numbers.size());
         return this.numbers.get(randomIndex);
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */