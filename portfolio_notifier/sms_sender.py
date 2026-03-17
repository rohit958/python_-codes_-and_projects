"""
SMS Sender Module
Supports multiple SMS providers: Twilio, MSG91, and Fast2SMS
"""

import os
import requests
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class SMSSender:
    """Unified SMS sender supporting multiple providers"""
    
    def __init__(self, provider: Optional[str] = None):
        """
        Initialize SMS sender
        
        Args:
            provider: SMS provider to use (twilio, msg91, fast2sms)
                     If None, reads from SMS_PROVIDER env variable
        """
        self.provider = provider or os.getenv('SMS_PROVIDER', 'twilio').lower()
        self.mobile_number = os.getenv('MOBILE_NUMBER')
        
        if not self.mobile_number:
            raise ValueError("MOBILE_NUMBER not set in environment variables")
        
        # Initialize provider-specific settings
        if self.provider == 'twilio':
            self._init_twilio()
        elif self.provider == 'msg91':
            self._init_msg91()
        elif self.provider == 'fast2sms':
            self._init_fast2sms()
        else:
            raise ValueError(f"Unsupported SMS provider: {self.provider}")
    
    def _init_twilio(self):
        """Initialize Twilio client"""
        try:
            from twilio.rest import Client
            
            account_sid = os.getenv('TWILIO_ACCOUNT_SID')
            auth_token = os.getenv('TWILIO_AUTH_TOKEN')
            self.twilio_phone = os.getenv('TWILIO_PHONE_NUMBER')
            
            if not all([account_sid, auth_token, self.twilio_phone]):
                raise ValueError("Twilio credentials not properly configured")
            
            self.twilio_client = Client(account_sid, auth_token)
            print("✓ Twilio initialized successfully")
        except ImportError:
            raise ImportError("Twilio library not installed. Run: pip install twilio")
    
    def _init_msg91(self):
        """Initialize MSG91 settings"""
        self.msg91_auth_key = os.getenv('MSG91_AUTH_KEY')
        self.msg91_sender_id = os.getenv('MSG91_SENDER_ID', 'MSGIND')
        self.msg91_route = os.getenv('MSG91_ROUTE', '4')
        
        if not self.msg91_auth_key:
            raise ValueError("MSG91_AUTH_KEY not set in environment variables")
        
        print("✓ MSG91 initialized successfully")
    
    def _init_fast2sms(self):
        """Initialize Fast2SMS settings"""
        self.fast2sms_api_key = os.getenv('FAST2SMS_API_KEY')
        
        if not self.fast2sms_api_key:
            raise ValueError("FAST2SMS_API_KEY not set in environment variables")
        
        print("✓ Fast2SMS initialized successfully")
    
    def send_sms(self, message: str) -> dict:
        """
        Send SMS using configured provider
        
        Args:
            message: Message text to send
            
        Returns:
            dict: Response with status and message_id
        """
        try:
            if self.provider == 'twilio':
                return self._send_twilio(message)
            elif self.provider == 'msg91':
                return self._send_msg91(message)
            elif self.provider == 'fast2sms':
                return self._send_fast2sms(message)
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'provider': self.provider
            }
    
    def _send_twilio(self, message: str) -> dict:
        """Send SMS via Twilio"""
        try:
            msg = self.twilio_client.messages.create(
                body=message,
                from_=self.twilio_phone,
                to=self.mobile_number
            )
            return {
                'success': True,
                'message_id': msg.sid,
                'provider': 'twilio',
                'status': msg.status
            }
        except Exception as e:
            raise Exception(f"Twilio error: {str(e)}")
    
    def _send_msg91(self, message: str) -> dict:
        """Send SMS via MSG91"""
        url = "https://api.msg91.com/api/v5/flow/"
        
        # Remove country code if present for MSG91
        mobile = self.mobile_number.replace('+91', '').replace('+', '')
        
        payload = {
            'sender': self.msg91_sender_id,
            'route': self.msg91_route,
            'country': '91',
            'sms': [
                {
                    'message': message,
                    'to': [mobile]
                }
            ]
        }
        
        headers = {
            'authkey': self.msg91_auth_key,
            'content-type': 'application/json'
        }
        
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            
            result = response.json()
            return {
                'success': True,
                'message_id': result.get('request_id', 'unknown'),
                'provider': 'msg91',
                'response': result
            }
        except Exception as e:
            raise Exception(f"MSG91 error: {str(e)}")
    
    def _send_fast2sms(self, message: str) -> dict:
        """Send SMS via Fast2SMS"""
        url = "https://www.fast2sms.com/dev/bulkV2"
        
        # Remove country code if present
        mobile = self.mobile_number.replace('+91', '').replace('+', '')
        
        payload = {
            'route': 'q',
            'message': message,
            'language': 'english',
            'flash': 0,
            'numbers': mobile
        }
        
        headers = {
            'authorization': self.fast2sms_api_key,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cache-Control': 'no-cache'
        }
        
        try:
            response = requests.post(url, data=payload, headers=headers)
            response.raise_for_status()
            
            result = response.json()
            return {
                'success': result.get('return', False),
                'message_id': result.get('request_id', 'unknown'),
                'provider': 'fast2sms',
                'response': result
            }
        except Exception as e:
            raise Exception(f"Fast2SMS error: {str(e)}")


def test_sms():
    """Test SMS sending with a simple message"""
    try:
        sender = SMSSender()
        test_message = "🧪 Test message from Portfolio Notifier"
        
        print(f"\nSending test SMS via {sender.provider}...")
        print(f"To: {sender.mobile_number}")
        print(f"Message: {test_message}\n")
        
        result = sender.send_sms(test_message)
        
        if result.get('success'):
            print("✅ SMS sent successfully!")
            print(f"Message ID: {result.get('message_id')}")
        else:
            print("❌ Failed to send SMS")
            print(f"Error: {result.get('error')}")
        
        return result
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return {'success': False, 'error': str(e)}


if __name__ == "__main__":
    test_sms()
