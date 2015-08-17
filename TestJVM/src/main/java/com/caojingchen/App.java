package com.caojingchen;
import java.util.*;
public class App 
{
	private static List<byte[]> list = new ArrayList<byte[]>();

	public static void main(String[] args) throws InterruptedException {
		while(true){
			Thread.currentThread().sleep(20);
			byte[] bytes = new byte[10240];
			if(list.size()< 10000)
				list.add(bytes);
	 		else
				list.clear();
		}
	}
}
