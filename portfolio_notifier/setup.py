#!/usr/bin/env python3
"""
Setup Helper Script
Guides users through initial configuration
"""

import os
import sys
from pathlib import Path


def print_header(text):
    """Print formatted header"""
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70 + "\n")


def print_step(num, text):
    """Print step number"""
    print(f"\n{'─' * 70}")
    print(f"STEP {num}: {text}")
    print('─' * 70)


def check_env_file():
    """Check if .env file exists"""
    if os.path.exists('.env'):
        print("✅ .env file found")
        return True
    else:
        print("❌ .env file not found")
        print("\nCreating .env from template...")
        
        if os.path.exists('.env.example'):
            import shutil
            shutil.copy('.env.example', '.env')
            print("✅ .env file created from .env.example")
            print("\n⚠️  IMPORTANT: Edit .env file with your actual credentials!")
            return False
        else:
            print("❌ .env.example not found. Please create .env manually.")
            return False


def check_dependencies():
    """Check if required dependencies are installed"""
    print("Checking dependencies...")
    
    missing = []
    required = [
        'selenium',
        'webdriver_manager', 
        'requests',
        'twilio',
        'schedule',
        'yaml',
        'dotenv'
    ]
    
    for package in required:
        try:
            __import__(package.replace('-', '_').replace('webdriver_manager', 'webdriver_manager'))
            print(f"  ✅ {package}")
        except ImportError:
            print(f"  ❌ {package}")
            missing.append(package)
    
    if missing:
        print(f"\n❌ Missing dependencies: {', '.join(missing)}")
        print("\nRun: pip install -r requirements.txt")
        return False
    else:
        print("\n✅ All dependencies installed")
        return True


def guide_sms_provider():
    """Guide user on SMS provider selection"""
    print_step(1, "SMS Provider Selection")
    
    print("""
Choose an SMS provider for notifications:

1. TWILIO (Recommended for testing)
   - International service
   - $15 trial credits
   - Excellent documentation
   - Sign up: https://www.twilio.com/try-twilio
   
2. MSG91 (Indian provider)
   - India-focused service
   - Competitive pricing for India
   - Sign up: https://msg91.com/signup
   
3. FAST2SMS (Indian provider)
   - Simple API
   - India only
   - Sign up: https://www.fast2sms.com/

After signing up, add credentials to .env file:
- Set SMS_PROVIDER to: twilio, msg91, or fast2sms
- Add corresponding API credentials
    """)


def guide_groww_setup():
    """Guide user on Groww credentials"""
    print_step(2, "Groww Credentials")
    
    print("""
Add your Groww login credentials to .env:

GROWW_EMAIL=your_email@example.com
GROWW_PASSWORD=your_password
GROWW_PIN=your_pin  # Only if you have PIN enabled

⚠️  SECURITY NOTES:
- .env file is gitignored - safe from version control
- Never share your .env file
- Use a strong, unique password
    """)


def guide_testing():
    """Guide user through testing"""
    print_step(3, "Testing")
    
    print("""
Test the system step by step:

1. Test SMS sending:
   $ python sms_sender.py
   
2. Test portfolio fetch (no SMS):
   $ python portfolio_notifier.py --dry-run --visible
   
3. Test end-to-end (sends SMS):
   $ python portfolio_notifier.py --send
   
4. Test scheduler (immediate):
   $ python scheduler.py --now
    """)


def guide_automation():
    """Guide user on automation setup"""
    print_step(4, "Enable Daily Automation")
    
    print("""
Run scheduler to get daily updates at 3:30 PM:

Option A - Foreground (terminal stays open):
$ python scheduler.py

Option B - Background (recommended):
$ nohup python scheduler.py > scheduler.out 2>&1 &

To check if running:
$ ps aux | grep scheduler.py

To view logs:
$ tail -f portfolio_notifier.log

To stop:
$ ps aux | grep scheduler.py
$ kill <process_id>
    """)


def main():
    """Main setup flow"""
    print_header("GROWW PORTFOLIO NOTIFIER - Setup Helper")
    
    print("""
This script will guide you through setting up the portfolio notifier.

Prerequisites:
✓ Python 3.7+ installed
✓ pip package manager
✓ Chrome browser installed
    """)
    
    input("Press Enter to continue...")
    
    # Check dependencies
    print_header("Dependency Check")
    deps_ok = check_dependencies()
    
    if not deps_ok:
        print("\n❌ Please install dependencies first:")
        print("   $ pip install -r requirements.txt")
        sys.exit(1)
    
    # Check .env file
    print_header("Configuration Check")
    env_exists = check_env_file()
    
    # Guide through setup
    guide_sms_provider()
    guide_groww_setup()
    
    # Testing guide
    guide_testing()
    
    # Automation guide
    guide_automation()
    
    # Summary
    print_header("Setup Complete!")
    
    if not env_exists:
        print("""
⚠️  NEXT STEPS:

1. Edit .env file with your Actual credentials:
   - Groww email, password, PIN
   - Mobile number (with country code +91...)
   - SMS provider credentials
   
2. Test SMS: python sms_sender.py

3. Test portfolio: python portfolio_notifier.py --dry-run --visible

4. Send real notification: python portfolio_notifier.py --send

5. Enable automation: python scheduler.py

For detailed documentation, see README.md
        """)
    else:
        print("""
✅ Configuration file exists.

QUICK START:
1. Test SMS: python sms_sender.py
2. Test portfolio: python portfolio_notifier.py --dry-run
3. Send notification: python portfolio_notifier.py --send
4. Enable automation: python scheduler.py

For detailed documentation, see README.md
        """)
    
    print("=" * 70)


if __name__ == "__main__":
    main()
