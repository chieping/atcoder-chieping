import java.util.Scanner;
import java.util.TreeSet;

public class MainTreeSet {
//public class Main {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var L = sc.nextInt();
        var Q = sc.nextInt();
        var set = new TreeSet<Integer>();
        set.add(0);
        set.add(L);
        for (int i = 0; i < Q; i++) {
            var c = sc.nextInt();
            var x = sc.nextInt();
            if (c == 1) {
                set.add(x);
            } else {
                int lower = set.lower(x);
                int higher = set.higher(x);
                System.out.println(higher - lower);
            }
        }
    }
}
