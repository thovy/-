package BAEKJOON;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class b10816 {
    public static void main(String[] args) throws IOException {
        // BufferedReader 를 사용하기 위해서는 IOException 을 던져줘야한단다.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 모든 수가 +- 1천만 까지기 때문에 int 를 하면 될 거 같다.
        // 카드 갯수 N
        // String 으로 받기 때문에 int 로
        int N = Integer.parseInt(br.readLine());

        // 카드에 적힌 숫자 number
        // String[] 으로 받게 됨
        int[] number = new int[N];
        String[] strNumber = br.readLine().split(" ");
//        System.out.println(strNumber);
//        System.out.println(strNumber[1]);

        // int[] 인 number 에 Stirng[] 인 strNumber 를 차례로 넣어주기
        for(int i = 0; i < N; i++){
            number[i] = Integer.parseInt(strNumber[i]);
        }
//        System.out.println(number);
//        System.out.println(number[8]);

        // 찾아볼 수 M
        int M = Integer.parseInt(br.readLine());

        // 검토해야할 M 개의 숫자들 matchingNumber
        String[] strMatchingNumber = br.readLine().split(" ");
        int[] matchingNumber = new int[M];
        for (int j = 0; j < M; j++){
            matchingNumber[j] = Integer.parseInt(strMatchingNumber[j]);
        }
//        System.out.println(matchingNumber[1]);

        // number 에 matchingNumber 가 몇 개가 있는지 나타낼 count ( 공백으로 구분해 출력 )
        List<String> list = new ArrayList<String>();
        for (int s = 0; s < N; s++){
            int count = 0;
            for(int m = 0; m < M; m++){
                if (number[s] == matchingNumber[m]){
                    count++;
                }
            }
            list.add(String.valueOf(count));
            if (s != N-1){
                list.add(" ");
            }
        }
        System.out.println(list);
    }
}
