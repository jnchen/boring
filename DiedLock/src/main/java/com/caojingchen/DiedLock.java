package com.caojingchen;
public class DiedLock{
	private String lock1 = "resource1";
	private String lock2 = "resource2";
	class Thread1 extends Thread{
		public void run(){
			synchronized(lock1){
				try{
					sleep(1000);
				}catch(InterruptedException e){
					e.printStackTrace();
				}
				synchronized(lock2){
					System.out.println("Have "+lock1+lock2);
				}
			}
		}
	}
	class Thread2 extends Thread{
		public void run(){
			synchronized(lock2){
				try{
					sleep(1000);
				}catch(InterruptedException e){
					e.printStackTrace();
				}
				synchronized(lock1){
					System.out.println("Have "+lock2+lock1);
				}
			}
		}
	}
	public static void main(String[] args){
		Thread1 th1 = new DiedLock().new Thread1();
		Thread2 th2 = new DiedLock().new Thread2();
		
		th1.start();
		th2.start();
	}
}
