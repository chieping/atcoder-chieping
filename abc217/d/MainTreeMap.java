import java.util.Scanner;
import java.util.TreeMap;

public class MainTreeMap {
//public class Main {
    public static void main(String[] args) {
        try (var sc = new Scanner(System.in)) {
            var L = sc.nextInt();
            var Q = sc.nextInt();

            var map = new TreeMap<Integer, Integer>();
            map.put(0, L);
            var sb = new StringBuilder();

            for (int i = 0; i < Q; i++) {
                var q = sc.nextInt();
                var x = sc.nextInt();
                var key = map.floorKey(x);
                var value = map.get(key);

                if (q == 1) {
                    map.put(key, x - key);
                    map.put(x, key + value - x);
                } else {
                    sb.append(value);
                    sb.append("\n");
                }
            }
            System.out.println(sb);
        }
    }
}
