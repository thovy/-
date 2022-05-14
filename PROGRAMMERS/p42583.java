package PROGRAMMERS;

import java.util.Arrays;

public class p42583 {

    public static void main(String[] args) {

        int bridge_length = 2;      // 다리 길이, 최대로 올라갈 수 있는 트럭 수, 트럭이 다리를 지나는데 걸리는 시간.
        int weight = 10;        // 다리가 견딜 수 있는 무게
        int[] truck_weights = {7, 4, 5, 6};         // 트럭들의 무게
        System.out.println(solution(bridge_length,weight,truck_weights));

    }

    public static int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;     // 트럭이 다리를 모두 건너는 데 걸린 시간

        int[] bridge = new int[bridge_length];

        // 현재 배열(다리) 전체의 합(총 무게)
        int bridge_sum = 0;
        for (int sum : bridge) {
            bridge_sum += sum;
        }
        System.out.println("다리 총 무게");
        System.out.println(bridge_sum);
        // 총 무게 끝

        // 트럭이 다리로 건너가는 모습
        int truck_i = 0;
        int bridge_i= 0;
        int i = 0;
        while(truck_i + i < truck_weights.length){
            int j = 0;


            bridge[bridge_i+1] = bridge[bridge_i];

            i++;
        }






        System.out.println("걸린 시간");
        return answer;
    }

}
