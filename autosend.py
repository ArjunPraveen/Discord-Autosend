from http.client import HTTPSConnection 
from sys import stderr 
from json import dumps 
from time import sleep 
import os
import sys
from dotenv import load_dotenv
import time 
load_dotenv()
def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
    print('Send message') 
 
header_data = { 
    "content-type": "application/json", 
    "user-agent": "hello there", 
    "authorization": os.environ.get("user_token"), 
    "host": "discordapp.com", 
    "referer":  os.environ.get("channel_link")
} 
 
def get_connection(): 
    return HTTPSConnection("discordapp.com", 443) 
 
def send_message(conn, channel_id, message_data): 
    try: 
        conn.request("POST", f"/api/v6/channels/{channel_id}/messages", message_data, header_data) 
        resp = conn.getresponse() 
         
        if 199 < resp.status < 300: 
            print("Message sent...") 
            pass 
 
        else: 
            print(resp.status)
            stderr.write(f"Received HTTP {resp.status}: {resp.reason}\n")
            pass 
 
    except Exception as e: 
        stderr.write("Failed to send_message\n") 
        print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
 
def main(msg): 
    message_data = { 
        "content": msg, 
        "tts": "false", 
    } 
 
    send_message(get_connection(), os.environ.get("channel_id"), dumps(message_data)) 
 
if __name__ == '__main__': 
    #countdown(2700)
    while 1:
        main('test')
        countdown(120)
    
    
        
