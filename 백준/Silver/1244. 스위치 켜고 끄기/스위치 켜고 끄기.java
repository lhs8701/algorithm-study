import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static int N;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        N = Integer.parseInt(scanner.nextLine());
        int[] array = Arrays.stream(scanner.nextLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        int studentNum = Integer.parseInt(scanner.nextLine());
        for (int i = 0; i < studentNum; i++) {
            int[] input = Arrays.stream(scanner.nextLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
            int gender = input[0];
            int number = input[1];
            if (gender == 1) {
                performMale(array, number);
            } else {
                performFemale(array, number);
            }
        }
        printSwitch(array);
    }

    public static void performMale(int[] array, int number) {
        for (int i = 0; i < N; i++) {
            if ((i + 1) % number == 0) {
                array[i] = array[i] ^ 1;
            }
        }
    }


    public static void performFemale(int[] array, int number) {
        int pivot = number - 1;
        array[pivot] = array[pivot] ^ 1;
        for (int i = 1; i < N / 2; i++) {
            if (pivot - i < 0 || pivot + i >= N) {
                break;
            }
            if (array[pivot - i] == array[pivot + i]) {
                array[pivot - i] = array[pivot - i] ^ 1;
                array[pivot + i] = array[pivot + i] ^ 1;
            }else{
                break;
            }
        }
    }

    private static void printSwitch(int[] array) {
        for (int i = 0; i < N; i++) {
            System.out.print(array[i]);
            if (i % 20 == 19) {
                System.out.println();
            }
            else if (i + 1 < N){
                System.out.print(" ");
            }
        }
    }
}

