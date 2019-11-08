public boolean checkPermutation(String a, String b){
    // sliding window
    HashMap<Character, Integer> freq = new HashMap<>();

    for(char c in a.toCharArray()){
        freq.put(c, freq.getOrDefault(c, 0)+1);
    }

    for(char c in b.toCharArray()){
        int f = m.get(c)-1;
        if(f == 0){
            if(checkMatch(m)) return true;
        }
        m.put(c, f+1);
    }
}

public boolean checkMatch(HashMap<Character, Integer> m){
    for(char c in m.keySet()){
        if(m.get(c) != 0) return false;
    }
    return true;
}