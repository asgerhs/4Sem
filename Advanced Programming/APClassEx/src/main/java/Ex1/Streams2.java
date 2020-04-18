package Ex1;

import java.io.BufferedReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 *
 * @author asgerhs
 */
public class Streams2 {

    public static void main(String[] args) throws IOException {
        BufferedReader buffReader = Files.newBufferedReader(Paths.get("names.txt"), StandardCharsets.UTF_8);
        buffReader.lines()
                .sorted()
                .forEach(s -> System.out.println(s + " has " + s.length() + " letters"));

    }
}
