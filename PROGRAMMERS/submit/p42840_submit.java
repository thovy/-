package PROGRAMMERS.submit;

public class p42840_submit {

//    같은 코드로 채점한 결과가 있습니다.
//            정확성  테스트
//    테스트 1 〉	통과 (0.06ms, 77.9MB)
//    테스트 2 〉	통과 (0.07ms, 75.6MB)
//    테스트 3 〉	통과 (0.05ms, 72MB)
//    테스트 4 〉	통과 (0.05ms, 74MB)
//    테스트 5 〉	통과 (0.05ms, 73.3MB)
//    테스트 6 〉	통과 (0.05ms, 79.5MB)
//    테스트 7 〉	통과 (0.75ms, 71.8MB)
//    테스트 8 〉	통과 (0.16ms, 72.8MB)
//    테스트 9 〉	통과 (1.11ms, 72.5MB)
//    테스트 10 〉	통과 (0.34ms, 77MB)
//    테스트 11 〉	통과 (1.17ms, 79.8MB)
//    테스트 12 〉	통과 (1.14ms, 84.1MB)
//    테스트 13 〉	통과 (0.08ms, 75MB)
//    테스트 14 〉	통과 (0.71ms, 76.4MB)
//    채점 결과
//    정확성: 100.0
//    합계: 100.0 / 100.0



//    import java.util.*;
//
//    class Solution {
//        public int[] solution(int[] answers) {
//            int[] answer = {};
//            int[] st1 = {1,2,3,4,5};
//            int[] st2 = {2,1,2,3,2,4,2,5};
//            int[] st3 = {3,3,1,1,2,2,4,4,5,5};
//            int score1 = 0;
//            int score2 = 0;
//            int score3 = 0;
//
//            for (int i=0;i<answers.length;i++){
//                int a1 = i%5;
//                if (answers[i] == st1[a1]){
//                    score1 += 1;
//                }
//            }
//
//            for (int i=0;i<answers.length;i++){
//                int a2 = i%8;
//                if (answers[i] == st2[a2]){
//                    score2 += 1;
//                }
//            }
//
//            for (int i=0;i<answers.length;i++){
//                int a3 = i%10;
//                if (answers[i] == st3[a3]){
//                    score3 += 1;
//                }
//            }
//            int max = Math.max(Math.max(score1, score2), score3);
//
//            List<Integer> list = new ArrayList<Integer>();
//            if(score1==max)list.add(1);
//            if(score2==max)list.add(2);
//            if(score3==max)list.add(3);
//            if(list.isEmpty()) return new int[]{1,2,3};
//
//            answer = new int[list.size()];
//            int index = 0;
//            for(int value : list){answer[index++]=value;}
//
//            return answer;
//        }
//    }
}
