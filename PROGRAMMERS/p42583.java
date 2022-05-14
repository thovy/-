package PROGRAMMERS;

import java.util.Arrays;

public class p42583 {

    public static void main(String[] args) {

        int bridge_length = 100;      // 다리 길이, 최대로 올라갈 수 있는 트럭 수, 트럭이 다리를 지나는데 걸리는 시간.
        int weight = 100;        // 다리가 견딜 수 있는 무게
        int[] truck_weights = {10,10,10,10,10,10,10,10,10,10};         // 트럭들의 무게
        System.out.println(solution(bridge_length,weight,truck_weights));

    }

    public static int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;     // 트럭이 다리를 모두 건너는 데 걸린 시간

        // 다리에 있는 트럭
        int[] bridge = new int[bridge_length];
        // 현재 다리 무게

        int t_i =0;
        while(t_i < truck_weights.length){
            System.out.println("-----");
            int bridge_sum = 0;
            for (int sum1 : bridge) {
                bridge_sum += sum1;
            }
            System.out.println("무게확인1: "+bridge_sum);
            System.out.println("다리확인1: "+Arrays.toString(bridge));

            if(bridge_sum - bridge[bridge_length-1] + truck_weights[t_i] <= weight){
                for(int i = bridge_length-2; i>=0; i--){
                    bridge[i+1] = bridge[i];
                }
                bridge[0] = truck_weights[t_i];
                System.out.println("다리확인2: "+Arrays.toString(bridge));
                t_i++;
                answer++;
            }else{
                for(int i = bridge_length-2; i>=0; i--){
                    bridge[i+1] = bridge[i];
                    bridge[0] = 0;
                }
                answer++;
            }

            for (int sum2 : bridge) {
                bridge_sum += sum2;
            }
            System.out.println("다리확인3: "+Arrays.toString(bridge));
            System.out.println("무게확인2: "+bridge_sum);
        }

        answer += bridge_length;
        System.out.println("걸린 시간");
        return answer;
    }

}
