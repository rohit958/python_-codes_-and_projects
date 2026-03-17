"""
Portfolio Notifier - Main Module
Combines portfolio fetching and SMS notification
"""

import os
import argparse
from datetime import datetime
from typing import Dict
from dotenv import load_dotenv

from groww_fetcher import GrowwPortfolioFetcher
from sms_sender import SMSSender

# Load environment variables
load_dotenv()


class PortfolioNotifier:
    """Main class to fetch portfolio data and send notifications"""
    
    def __init__(self, dry_run: bool = False):
        """
        Initialize portfolio notifier
        
        Args:
            dry_run: If True, don't send SMS, just print the message
        """
        self.dry_run = dry_run
        self.portfolio_fetcher = None
        self.sms_sender = None
        
        if not dry_run:
            try:
                self.sms_sender = SMSSender()
            except Exception as e:
                print(f"⚠️ Warning: SMS sender initialization failed: {e}")
                print("Running in dry-run mode instead")
                self.dry_run = True
    
    def format_notification_message(self, portfolio_data: Dict) -> str:
        """
        Format portfolio data into SMS notification message
        
        Args:
            portfolio_data: Portfolio data dictionary
            
        Returns:
            str: Formatted SMS message
        """
        if 'error' in portfolio_data:
            return f"❌ Portfolio Error: {portfolio_data['error']}"
        
        current_value = portfolio_data.get('current_value', 0)
        today_gain = portfolio_data.get('today_gain', 0)
        today_gain_pct = portfolio_data.get('today_gain_percent', 0)
        
        # Determine emoji based on gain/loss
        if today_gain > 0:
            emoji = "📈 ✅"
            status = "GAIN"
        elif today_gain < 0:
            emoji = "📉 ⚠️"
            status = "LOSS"
        else:
            emoji = "➡️"
            status = "UNCHANGED"
        
        # Format the message
        message = f"""
{emoji} Groww Portfolio Update

TODAY'S {status}:
₹{abs(today_gain):,.2f} ({today_gain_pct:+.2f}%)

CURRENT VALUE:
₹{current_value:,.2f}

Time: {datetime.now().strftime('%I:%M %p, %d %b %Y')}
        """.strip()
        
        return message
    
    def run(self, headless: bool = True) -> Dict:
        """
        Main execution: fetch portfolio and send notification
        
        Args:
            headless: Run browser in headless mode
            
        Returns:
            dict: Result with portfolio data and notification status
        """
        result = {
            'success': False,
            'portfolio_data': {},
            'notification': {},
            'timestamp': datetime.now().isoformat()
        }
        
        try:
            print("=" * 70)
            print(" " * 15 + "GROWW PORTFOLIO NOTIFIER")
            print("=" * 70)
            print(f"Mode: {'DRY RUN (No SMS)' if self.dry_run else 'LIVE'}")
            print(f"Time: {datetime.now().strftime('%I:%M %p, %d %B %Y')}")
            print("=" * 70)
            
            # Step 1: Fetch portfolio data
            print("\n📊 STEP 1: Fetching Portfolio Data")
            print("-" * 70)
            
            self.portfolio_fetcher = GrowwPortfolioFetcher(headless=headless)
            portfolio_data = self.portfolio_fetcher.get_portfolio_summary()
            
            result['portfolio_data'] = portfolio_data
            
            if 'error' in portfolio_data:
                print(f"\n❌ Failed to fetch portfolio data: {portfolio_data['error']}")
                return result
            
            # Step 2: Format notification message
            print("\n✉️ STEP 2: Formatting Notification")
            print("-" * 70)
            
            message = self.format_notification_message(portfolio_data)
            print("\nMessage Preview:")
            print("┌" + "─" * 68 + "┐")
            for line in message.split('\n'):
                print(f"│ {line:<66} │")
            print("└" + "─" * 68 + "┘")
            
            # Step 3: Send notification
            print("\n📱 STEP 3: Sending Notification")
            print("-" * 70)
            
            if self.dry_run:
                print("⏭️ SKIPPED (Dry Run Mode)")
                result['notification'] = {
                    'success': True,
                    'dry_run': True,
                    'message': 'SMS not sent - dry run mode'
                }
            else:
                print(f"Sending SMS via {self.sms_sender.provider}...")
                notification_result = self.sms_sender.send_sms(message)
                result['notification'] = notification_result
                
                if notification_result.get('success'):
                    print(f"✅ SMS sent successfully!")
                    print(f"Message ID: {notification_result.get('message_id', 'N/A')}")
                else:
                    print(f"❌ Failed to send SMS: {notification_result.get('error')}")
            
            result['success'] = True
            
            # Summary
            print("\n" + "=" * 70)
            print(" " * 25 + "SUMMARY")
            print("=" * 70)
            print(f"Current Value: ₹{portfolio_data.get('current_value', 0):,.2f}")
            print(f"Today's Change: ₹{portfolio_data.get('today_gain', 0):+,.2f} "
                  f"({portfolio_data.get('today_gain_percent', 0):+.2f}%)")
            print(f"Notification: {'Sent ✅' if result['notification'].get('success') else 'Failed ❌'}")
            print("=" * 70)
            
            return result
            
        except Exception as e:
            print(f"\n❌ CRITICAL ERROR: {str(e)}")
            result['error'] = str(e)
            return result


def main():
    """Main entry point with CLI arguments"""
    parser = argparse.ArgumentParser(
        description='Groww Portfolio Notifier - Get daily P&L updates via SMS',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python portfolio_notifier.py --dry-run     # Test without sending SMS
  python portfolio_notifier.py --send        # Fetch and send SMS
  python portfolio_notifier.py --visible     # Run with visible browser
        """
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Fetch portfolio data but do not send SMS'
    )
    
    parser.add_argument(
        '--send',
        action='store_true',
        help='Fetch portfolio data and send SMS notification'
    )
    
    parser.add_argument(
        '--visible',
        action='store_true',
        help='Show browser window (not headless)'
    )
    
    args = parser.parse_args()
    
    # Default to dry-run if neither flag is specified
    dry_run = not args.send
    headless = not args.visible
    
    # Run the notifier
    notifier = PortfolioNotifier(dry_run=dry_run)
    result = notifier.run(headless=headless)
    
    # Exit with appropriate code
    exit(0 if result.get('success') else 1)


if __name__ == "__main__":
    main()
