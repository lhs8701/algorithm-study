import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static int next(int curIdx, boolean[] array) {
        if (curIdx + 1 == array.length) {
            return 1;
        }
        return curIdx + 1;
    }

    public static int getNextIdx(int curIdx, boolean[] array) {
        while (true) {
            curIdx = next(curIdx, array);
            if (!array[curIdx]) {
                return curIdx;
            }
        }
    }

    public static void main(String[] args) {
        String input = new Scanner(System.in).nextLine();
        String[] token = input.split(" ");
        int N = Integer.parseInt(token[0]);
        int K = Integer.parseInt(token[1]);
        boolean[] array = new boolean[N + 1];
        Arrays.fill(array, false);

        int cur = 0;
        System.out.print("<");
        for (int i = 0; i < N - 1; i++) {
            for (int j = 0; j < K; j++) {
                cur = getNextIdx(cur, array);
            }
            array[cur] = true;
            System.out.print(cur + ", ");
        }
        System.out.println(getNextIdx(cur, array) + ">");
    }
}