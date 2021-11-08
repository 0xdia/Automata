import java.lang.System.*;

/*
  Implementing a determinitic finit automaton, to recognize the following language:
    
      alphabet = { 0, 1 }
      only strings that contain an even number of 0s, and an odd number of 1s

*/
/*
  There are 4 states:
    0: even number of 0s and even number of 1s => start state
    1: even number of 0s and odd number of 1s  => final state
    2: odd number of 0s and even number of 1s
    3: odd number of 0s and odd number of 1s 
*/

public class DFA {


  static boolean wordBelongsToLanguage(String word) {
    int startState = 0;
    int finalState = 1;

    int currentState = startState;

    int[][] transitionTable = {
                                {2, 1},
                                {3, 0},
                                {0, 3},
                                {1, 2}
                              };

    for (int i=0; i<word.length(); i++) {
      currentState = transitionTable[currentState][word.charAt(i)-'0'];
    }

    return currentState == finalState;
  }

  public static void main(String[] args) {
    String word = "00001";
    System.out.println(wordBelongsToLanguage(word));
  }
}
