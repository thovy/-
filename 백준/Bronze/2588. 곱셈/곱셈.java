import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scA = new Scanner(System.in);
        int A = Integer.parseInt(scA.nextLine());
        int B = Integer.parseInt(scA.nextLine());

        int remainB = B%10;
        System.out.println(A * remainB);
        System.out.println((A * ((B%100)-remainB))/10);
        System.out.println((A * ((B/100)*100))/100);
        System.out.println(A*B);
    }
}