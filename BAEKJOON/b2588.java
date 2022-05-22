package BAEKJOON;

import java.util.Scanner;

public class b2588 {
    public static void main(String[] args) {
        Scanner scA = new Scanner(System.in);
//        Scanner scB = new Scanner(System.in);

        int A = Integer.parseInt(scA.nextLine());
        int B = Integer.parseInt(scA.nextLine());

        int remainB = B%10;
        System.out.println(A * remainB);
        System.out.println((A * ((B%100)-remainB))/10);
        System.out.println((A * ((B/100)*100))/100);
        System.out.println(A*B);
    }

//    메모리 17572 KB
//    시간 204 ms
//    코드길이 457 B

}
