package Ex1;

import java.util.stream.Stream;

/**
 *
 * @author asgerhs
 */
public class FindKlaus {
    public static void main(String[] args) {
      Stream<String> names = Stream.of("Jørgen ","Karl ","Jens ","Hyben ","Flemming ","Gerda ","Karma ","Lone ","Linus ","Finn ","Dominik ","Jonas ","Jan ","Gertrud ","Gunhilde ","Rigmor ","Hans ","Lise");
      boolean result = names.noneMatch(str -> (str.equals("Klaus")));
        System.out.println(result);
    }
}
