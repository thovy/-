package PROGRAMMERS.submit;

public class p42568_submit {

//    채점을 시작합니다.
//    정확성  테스트
//    테스트 1 〉	통과 (3.00ms, 75.1MB)
//    테스트 2 〉	통과 (2.12ms, 76.4MB)
//    테스트 3 〉	통과 (2.13ms, 79.1MB)
//    테스트 4 〉	통과 (2.82ms, 75.8MB)
//    테스트 5 〉	통과 (1.95ms, 73.8MB)
//    테스트 6 〉	통과 (1.86ms, 74.5MB)
//    테스트 7 〉	통과 (2.17ms, 75.8MB)
//    테스트 8 〉	통과 (2.31ms, 82.4MB)
//    테스트 9 〉	통과 (2.05ms, 81MB)
//    테스트 10 〉	통과 (2.56ms, 75.7MB)
//    테스트 11 〉	통과 (1.95ms, 76.2MB)
//    채점 결과
//    정확성: 100.0
//    합계: 100.0 / 100.0

//    import java.util.*;
//
//    class Solution {
//        public int[] solution(int[] progresses, int[] speeds) {
//
//            List<String> tmpAnswer = new ArrayList<>();
//
//            int i = 0;
//            int countIndex = 0;
//
//            for(; i<progresses.length; i++){
//                int completedProgress = 0;
//
//                if(progresses[i] < 100){
//                    while(progresses[i]<100){
//                        for(int j =0; j<progresses.length;j++){
//                            progresses[j] += speeds[j];
//                        }
//                    }
//                    completedProgress++;
//                }
//
//
//                if (i+1>progresses.length-1){
//                }else if(progresses[i+1]<100){
//                }else if(progresses[i+1]>=100){
//                    completedProgress++;
//                    i++;
//                    int j = 1;
//                    while(i+j<progresses.length){
//                        if(progresses[i+j]>=100){
//                            completedProgress++;
//                            i++;
//                        }else{
//                            break;
//                        }
//                    }
//                }
//                tmpAnswer.add(countIndex, String.valueOf(completedProgress));
//                countIndex++;
//                System.out.println(tmpAnswer);
//            }
//
//            String[] tmparr = tmpAnswer.toArray(new String[0]);
//            int[] answer = Arrays.stream(tmparr).mapToInt(Integer::parseInt).toArray();
//            return answer;
//
//        }
//    }

}
