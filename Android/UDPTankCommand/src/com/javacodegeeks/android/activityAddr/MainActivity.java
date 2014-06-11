package com.javacodegeeks.android.activityAddr;

import android.os.Bundle;
import android.os.Handler;
import android.annotation.SuppressLint;
import android.app.Activity;
import android.content.BroadcastReceiver;
import android.content.Context;

import java.io.IOException;
import java.net.SocketTimeoutException;
import java.io.OutputStream;
import java.io.InputStream;

import com.javacodegeeks.android.activityAddr.R;

import android.content.Intent;
import android.content.IntentFilter;
import android.content.pm.ActivityInfo;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import java.net.DatagramPacket; 
import java.net.DatagramSocket;
import java.net.InetAddress;


public class MainActivity extends Activity {

	   @SuppressLint ("NewApi")
	   int myApp = 0;
	   int myParam = 0;
	   String myDescription = "";
	   int requestIndex = 0; 
		
	   private TextView text;   
	   private Button btnLeft;
	   private Button btnRight;
	   private Button btnUp;
	   private Button btnDown;
	   private Button btnFire;
	   private Button btnTurretRight;
	   private Button btnTurretLeft;
	   private Button btnUpDown;
	   private Button btnReset;
       private String lastMessage = "";
	   
	   
	   private MyDatagramReceiver myDatagramReceiver;
       	   
	   
	   @Override
	   protected void onCreate(Bundle savedInstanceState) {
	      super.onCreate(savedInstanceState);
	      int orientation = ActivityInfo.SCREEN_ORIENTATION_PORTRAIT;
	      setRequestedOrientation (orientation);
	      setContentView(R.layout.piclient_activity);
	      
	 	  text = (TextView) findViewById(R.id.textView1);
	      text.setText ( "Commander Ready");   	         
	      
 	      myDatagramReceiver = new MyDatagramReceiver();
 	      myDatagramReceiver.start();
	      
	      
	      btnLeft = (Button)findViewById(R.id.btnLeft);	      
	      btnLeft.setOnClickListener(new OnClickListener() {  		
    	    @SuppressLint("NewApi")
	  		public void onClick(View v) {	    	    		    		   
	    		   myDatagramReceiver.sendMessage ("left     "); 
              }
	        });
	      
	      btnRight = (Button)findViewById(R.id.btnRight);
	      btnRight.setOnClickListener(new OnClickListener() {  		
	    	@SuppressLint("NewApi")
	  		public void onClick(View v) {
	    		   myDatagramReceiver.sendMessage ("right     "); 
	        }
	      });
	      
	      btnUp = (Button)findViewById(R.id.btnUp);
	      btnUp.setOnClickListener(new OnClickListener() {  		
	    	@SuppressLint("NewApi")
	  		public void onClick(View v) {
	    		   myDatagramReceiver.sendMessage ("forward    ");
	        }
	      });
	      
	      btnDown = (Button)findViewById(R.id.btnDown);
	      btnDown.setOnClickListener(new OnClickListener() {  		
	    	@SuppressLint("NewApi")
	  		public void onClick(View v) {
	    		   myDatagramReceiver.sendMessage ("reverse   "); 
	        }
	      });
	      
	       	      
	      btnFire = (Button)findViewById(R.id.btnFire);
	      btnFire.setOnClickListener(new OnClickListener() {  		
	    	@SuppressLint("NewApi")
	  		public void onClick(View v) {
	    		   myDatagramReceiver.sendMessage ("fire      "); 
	        }
	      });
	      
	      btnTurretLeft = (Button)findViewById(R.id.btnTurretLeft);
	      btnTurretLeft.setOnClickListener(new OnClickListener() {  		
	    	@SuppressLint("NewApi")
	  		public void onClick(View v) {
	    		   myDatagramReceiver.sendMessage ("TLeft"); 
	        }
	      });
	      
	      btnTurretRight = (Button)findViewById(R.id.btnTurretRight);
	      btnTurretRight.setOnClickListener(new OnClickListener() {  		
	    	@SuppressLint("NewApi")
	  		public void onClick(View v) {
	    		   myDatagramReceiver.sendMessage ("TRight"); 
	        }
	      });

	      btnUpDown = (Button)findViewById(R.id.btnUpDown);
	      btnUpDown.setOnClickListener(new OnClickListener() {  		
	    	@SuppressLint("NewApi")
	  		public void onClick(View v) {
	    		   myDatagramReceiver.sendMessage ("TUpDown"); 
	        }
	      });

	      btnReset = (Button)findViewById(R.id.btnReset);
	      btnReset.setOnClickListener(new OnClickListener() {  		
	    	@SuppressLint("NewApi")
	  		public void onClick(View v) {
	    		   myDatagramReceiver.sendMessage ("reset"); 
	        }
	      });
	        
	            
	   }
	   
	   
	   @Override
	   protected void onDestroy() {
		   // TODO Auto-generated method stub
		   myDatagramReceiver.kill();		   
		   super.onDestroy();
	   }
	   
	   
	   private class MyDatagramReceiver extends Thread {
		    
		    private boolean bKeepRunning = true;
		    private String newMessage = "";
		    private int msgNumber = 0;
		    private int lastMsgNumber = 0;
			private DatagramSocket socket = null;
			private String hostName = "172.16.0.23"; // "172.16.0.12";
			private int hostPort = 5000; // 3333;

		    public void sendMessage ( String msg ) {
	  			newMessage = msg;
	  			text.setText (msg);
	  			incrementMessage();
	   		    // txtMtgCommand.setText (msg);	  			
		    }
		    
		    public void incrementMessage () {
		    	msgNumber = msgNumber + 1;
		    }
		    
		    /*
		    private void checkResponse (int timeout) {
		       String message;
		       try {
  			     InetAddress serverAddr = InetAddress.getByName(hostName); 
   			     DatagramPacket sendPacket;
    			 byte[] lmessage = new byte[5000];
   	  		     DatagramPacket receivePacket = new DatagramPacket(lmessage, lmessage.length);
     		     socket = null;
     		     socket = new DatagramSocket(hostPort);
        		 sendPacket = null;
			     message = "ping";
			     sendPacket = new DatagramPacket ( message.getBytes(), message.length(), serverAddr, hostPort);
     		     socket.send(sendPacket);	
     		     boolean soTimeout = false;
     		     try {
     		       socket.setSoTimeout(timeout);
     		       //socket.setReuseAddress(true);
     		       socket.receive(receivePacket);
     		     } catch (SocketTimeoutException s) {
     	  		   soTimeout = true;
     		     } 
     		   
       		     String info = new String(receivePacket.getData());
     		     if (soTimeout)   {
         		    //message = new String ( "No check response");
         		    //lastMessage = message;
         		    //runOnUiThread(updateTextMessage);
     		     }
     		     else {
         		    lastMessage = info;
         		    runOnUiThread(updateTextMessage);
     		     }
     		     socket.close();		    
		       } catch (Exception e){
		       
		       }
		    }
		    */		    
		    public void run() {
		    	
		        String message;
    			try {
       			   InetAddress serverAddr = InetAddress.getByName(hostName); 
       			   DatagramPacket sendPacket;
       			   byte[] lmessage = new byte[5000];
       			   DatagramPacket receivePacket;
       			   
       			   // Kludgy udp flush
				   //checkResponse(100);
				   //checkResponse(100);
   				   //checkResponse(100);
   				   //checkResponse(100);
   				   //checkResponse(100);

       			   while(bKeepRunning) {
       				   try {
       					   if (msgNumber == lastMsgNumber)
       					   {	 
       						   //checkResponse(100);
       					   }	   
       					   else // if (msgNumber != lastMsgNumber)
		            	   {
		            		   lastMsgNumber = msgNumber;
		            		   sendPacket = null;
              			       sendPacket = new DatagramPacket ( newMessage.getBytes(), newMessage.length(), serverAddr, hostPort);
		            		   socket = null;
		            		   socket = new DatagramSocket(hostPort);
		            		   socket.send(sendPacket);	
		            		   boolean soTimeout = false;
		            		   receivePacket = null;
		            		   for (int i=0; i<32; i++)
		            		      lmessage [i] = ' ';
		            		   receivePacket = new DatagramPacket(lmessage, lmessage.length);
		            		   try {
		            		     socket.setSoTimeout(300);
		            		     socket.setReuseAddress(true);
		      	
		            		     socket.receive(receivePacket);
		            		   } catch (SocketTimeoutException s) {
		            			 soTimeout = true;
		            		   } 
		            		   
		            		   String info = new String(receivePacket.getData());
		            		   if (soTimeout)   {
			            		  message = new String ( "soTimeout, No response");
			            		  lastMessage = message;
			            		  runOnUiThread(updateTextMessage);
		            		   }
		            		   else {
			            		  lastMessage = info;
			            		  runOnUiThread(updateTextMessage);
		            		   }
		            		   socket.close();
		            	   }
       				   } catch (Throwable e) {
       					   e.printStackTrace();
       					   Log.e ("UDP", "D: Error", e);
       				   }
       			   }
		        
    			} catch (Exception e) {
    				Log.e("UDP", "C: Error", e);
    			}       			   
    			

		    }

		    public void kill() { 
		        bKeepRunning = false;
		        socket.close();
		    }

		    public String getLastMessage() {
		        return lastMessage;
		    }
		}
		
	  

  	   
	   private Runnable updateTextMessage = new Runnable() {
		    public void run() {
		    	String msg = myDatagramReceiver.getLastMessage().trim();
		    	//String newMsg = msg.concat("     ");
		    	/*
		    	int value;
		    	if ( requestIndex == 1) {
		    		value = Integer.parseInt(msg); // substring (0) ?
		    		if ((value & 8) != 0)
		    			msg = msg.concat(" Antenna Good");
		            else
		            	msg = msg.concat (" Antenna Bad");
		    	}
		    	*/
		    	requestIndex = 0;
		    	text.setText(msg);
       		    //byte bytes[] = {0};
     		    // receivePacket.setData(bytes);
		    }
		};
		
	  }
