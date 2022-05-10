package PROGRAMMERS;

import java.util.Arrays;

public class p42584 {
    public static void main(String[] args) {

        int[] prices = {1,2,3,2,3};
        System.out.println(Arrays.toString(solution(prices)));

    }

    // static 안하면 main에서 solution 메소드를 읽지 못 하는 듯함.
    public static int[] solution(int[] prices) {
        int[] answer = new int[prices.length];

        // for 문이 두 개 밖에 없는데도 이해가 안 돼서 출력문으로 구분해줌.
        // prices[3], prices[4] 가 도저히 계산이 안됐음.
        // 하지만 구분해서 출력해가지고 살펴보니 이해 완료. 끄덕.
        for (int i = 0; i < prices.length; i++){
            int second = 0;
            for (int j = i+1; j < prices.length; j++){
                if (prices[i] <= prices[j]){
                    second++;
                    System.out.println(i +" true- "+ second+" 초");
                }else{
                    second++;
                    answer[i] = second;
                    System.out.println(i +" - "+ second+" 초 끝");
                    break;
                }
                answer[i] = second;
                System.out.println("총 " + Arrays.toString(answer));
            }
            answer[i] = second;
            System.out.println("총 " + Arrays.toString(answer)+" 끝");
        }


        return answer;
    }

}
