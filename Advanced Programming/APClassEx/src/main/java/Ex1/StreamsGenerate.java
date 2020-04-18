package Ex1;

import java.util.Random;
import java.util.stream.Stream;

/**
 *
 * @author asgerhs
 */
public class StreamsGenerate {

    public static void main(String[] args) {
       
       Stream.generate(() -> (new Random()).nextInt(11)).limit(100).distinct().forEach(System.out::println);
       
       

    }
}
