package PROGRAMMERS;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class p42586 {
    public static void main(String[] args) {
        int[] progresses = {95, 90, 99, 99, 80, 90};
        int[] speeds = {1, 1, 1, 1, 1, 1};
        System.out.println(Arrays.toString(solution(progresses, speeds)));
    }

    public static int[] solution(int[] progresses, int[] speeds) {

        List<String> tmpAnswer = new ArrayList<>();

        int i = 0;

        for(; i< progresses.length; i++){
            int completedProgress = 0;

            if(progresses[i] < 100){
                // i 가 작으면 전체 progresses 값에 speeds 값 더하기.
                // 완료되면 completedProgress++
                while(progresses[i]<100){
                    for(int j = 0; j< progresses.length; j++){
                        progresses[j] += speeds[j];
                    }
                }
                // for 문으로 하나 완료했으니 ++
                completedProgress++;
                System.out.println("if문 확인");
                System.out.println(Arrays.toString(progresses));
                System.out.println(completedProgress);
            }

            System.out.println("if문 완료");
            System.out.println(Arrays.toString(progresses));
            System.out.println(completedProgress);


            // i 다음 값으로 completedProgress 올리기
            for (int j=i+1;progresses[i]>=100;j++){
                if(j>progresses.length){
                    break;
                }else if(progresses[j]>=100){
                    completedProgress++;
                }else{
                    break;
                }
            }
            System.out.println("count 확인");
            System.out.println(Arrays.toString(progresses));
            System.out.println(completedProgress);


            // compleawtedProgress 값 tmpAnswer 에 넣어주기.
            tmpAnswer.add(i, String.valueOf(completedProgress));

        }
        System.out.println("for문 끝");
        System.out.println(tmpAnswer);



        int[] answer = new int[tmpAnswer.size()];
        return answer;

    }


}
