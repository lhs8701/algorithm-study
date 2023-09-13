import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st1 = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st1.nextToken());
        int b = Integer.parseInt(st1.nextToken());

        StringTokenizer st2 = new StringTokenizer(br.readLine());
        int c = Integer.parseInt(st2.nextToken());
        int d = Integer.parseInt(st2.nextToken());

        int x = lcm(b, d);
        int e = x / b;
        int f = x / d;
        int y = a * e + c * f;
        int z = gcm(x, y);
        System.out.println(y / z + " " + x / z);
    }

    public static int gcm(int num1, int num2) {
        if (num1 < num2) {
            int temp = num1;
            num1 = num2;
            num2 = temp;
        }
        while (num2 != 0) {
            int temp = num1 % num2;
            num1 = num2;
            num2 = temp;
        }
        return num1;
    }

    public static int lcm(int num1, int num2) {
        int smaller = Math.min(num1, num2);
        int larger = Math.max(num1, num2);
        for (int i = 1; i <= larger; i++) {
            if (smaller * i % larger == 0) {
                return smaller * i;
            }
        }
        return -1;
    }
}

