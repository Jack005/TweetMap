/* Yunxuan Zhu
 * yz2868
 * Problem1.java
 */

//Problem1 class
public class Problem1{
    public static void main(String[] args){
    	//instantiates expressionTree
        ExpressionTree eTree = new ExpressionTree("32 2 - 5 * 4 + 2 /");
        System.out.println("Input postfix expression: 32 2 - 5 * 4 + 2 /");
        System.out.println("Evaluation: " + eTree.eval());
        System.out.println("Postfix expression: " + eTree.postfix());
        System.out.println("Prefix expression: " + eTree.prefix());
        System.out.println("Infix expression: " + eTree.infix());
    }
}