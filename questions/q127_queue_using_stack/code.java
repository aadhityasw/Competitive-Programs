import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int q = sc.nextInt();
        
        int stack1[] = new int[q];
        int stack2[] = new int[q];
        int numEle1 = 0, numEle2 = 0;
        
        int cho, ele;
        for(int qu=0; qu<q; qu++) {
            cho = sc.nextInt();
            
            if (cho == 1) {
                stack1[numEle1] = sc.nextInt();
                numEle1 ++;
            }
            else if (cho == 2) {
                while (numEle1 > 0) {
                    stack2[numEle2++] = stack1[numEle1--];
                }
                // Ignore the top element
                numEle2 --;
                // Transfer the remaining back to stack1
                while (numEle2 > 0) {
                    stack1[numEle1++] = stack2[numEle2--];
                }
            }
            else if (cho == 3) {
                System.out.println(stack1[0]);
            }
        }
    }
}
