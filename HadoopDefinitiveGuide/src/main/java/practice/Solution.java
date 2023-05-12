package practice;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public String countAndSay(int n) {
        if (n == 1) {
            return "1";
        }
        List<String> ret = new ArrayList<String>();
        int cnt = 0;
        while (cnt <= n) {
            ret.add("1");
            n--;
            cnt++;
        }
        return "";// 370330210033463
    }
}
