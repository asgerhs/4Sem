package Ex1;
import java.util.*; 
import java.util.stream.*; 

/**
 *
 * @author asgerhs
 */
public class Streams {
    public static void main(String[] args) {
        String[] strings = {"10","11", "12","13","14","15"};
        List<String> numsList = Arrays.asList(strings);
        int result = numsList.stream()
                .map(x -> Integer.parseInt(x))
                .filter(x -> x % 2 == 1)
                .reduce(0, (sum, x) -> sum + x);
        System.out.println(result);
    }
}
