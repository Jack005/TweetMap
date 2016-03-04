/* Yunxuan Zhu
 * yz2868
 * Problem2.java
 */

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

//Problem2 class
public class Problem2 {
	public static void main(String[] args) throws IOException{
		//instantiates AvlTree
		AvlTree<String> t = new AvlTree<>();
		//read file
		FileInputStream fileInput = new FileInputStream(args[0]);
		BufferedReader bufferRead = new BufferedReader(new InputStreamReader(fileInput));
		
    	String line;
    	int i=1;
    	
    	//read line by line
    	while ((line = bufferRead.readLine()) != null){
    		//check empty line
    		if (line.trim().equals("") == false){
    		line=line.toLowerCase();
    		line = line.replaceAll("\\p{Punct}+","");
    		String charIn[] = line.split(" ");
    		
    		for (int j=0; j < charIn.length; j++){
    			if (charIn[j].matches("\\w+")){
    				t.insert(charIn[j], Integer.toString(i));
    			}
    		}
    		}
    		i++;
    	}
    	
    	//close file
		bufferRead.close();
		
		//print AvlTree
		t.printTree();
	}
}
