from http.client import HTTPSConnection 
from sys import stderr 
from json import dumps 
from time import sleep 
import os
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
    "authorization": os.environ.get("user-token"), 
    "host": "discordapp.com", 
    "referer":  os.environ.get("channel-link")
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
            stderr.write(f"Received HTTP {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Failed to send_message\n") 
 
def main(msg): 
    message_data = { 
        "content": msg, 
        "tts": "false", 
    } 
 
    send_message(get_connection(), os.environ.get("channel-id"), dumps(message_data)) 
 
if __name__ == '__main__': 
    #countdown(2700)
    main('test')
    
    
        