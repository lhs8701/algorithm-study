import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] array = new int[N];
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());
            array[i] = num;
        }
        Arrays.sort(array);
        long sum = 0;
        for (int i = 0; i < N; i++) {
            int rank = i + 1;
            sum += Math.abs(rank - array[i]);
        }
        System.out.println(sum);
    }
}

