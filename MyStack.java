/* Yunxuan Zhu
 * yz2868
 * MyStack.java
 */

import java.util.LinkedList;

//generic
public class MyStack<T> {
	//declare variables
	private LinkedList<T> newStack;
	
	//constructor
	public MyStack(){
		newStack = new LinkedList<T>();
	}
	
	//push method
	public void push(T b){
		newStack.addFirst(b);
	}
	
	//pop method
	public T pop(){
		return newStack.removeFirst();
	}
	
	//top method
	public T top(){
		return newStack.getFirst();
	}
	
	//check empty stack method
	public boolean isEmpty(){
		if (newStack.peekFirst()==null){
			return true;
		}
		else{
			return false;
			}
	}
}
