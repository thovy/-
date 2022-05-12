package PROGRAMMERS;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class p42586 {
    public static void main(String[] args) {
        int[] progresses = {93, 30, 55};
        int[] speeds = {1, 30, 5};
        System.out.println(Arrays.toString(solution(progresses, speeds)));
    }

    public static int[] solution(int[] progresses, int[] speeds) {

        List<String> tmpAnswer = new ArrayList<>();

        int i = 0;
        int countIndex = 0;

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
            if (i+1>progresses.length-1){
                // 아무것도 안해도 break 됨 다음 i가 progress.length 보다 길테니까
            }else if (progresses[i+1]<100){
                // 아무것도 안해야 됨.
            }else if (progresses[i+1]>=100){
                completedProgress++;
                i++;
                int j = 1;
                while(i+j<progresses.length){
                    if (progresses[i+j]>=100){
                        completedProgress++;
                        i++;
                    }else{
                        break;
                    }
                }
            }

            System.out.println("count 확인");
            System.out.println(Arrays.toString(progresses));
            System.out.println(completedProgress);


            // compleawtedProgress 값 tmpAnswer 에 넣어주기.
            System.out.println("tmpAnswer 에 넣기");
            tmpAnswer.add(countIndex, String.valueOf(completedProgress));
            countIndex++;
            System.out.println(tmpAnswer);

        }
        System.out.println("for문 끝");
        System.out.println(tmpAnswer);

        // List<String> 을 String[] 으로
        String[] tmparr = tmpAnswer.toArray(new String[0]);
        // String[] 을 int[] 로 바꾸면서 answer 에 넣기
        int[] answer = Arrays.stream(tmparr).mapToInt(Integer::parseInt).toArray();
        return answer;

    }


}
