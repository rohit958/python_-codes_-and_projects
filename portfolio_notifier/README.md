# Groww Portfolio Notifier 📱📈

Automated notification system that sends daily portfolio gain/loss updates from Groww to your mobile via SMS.

## Features

- 🔐 **Secure Login**: Automated login to Groww using Selenium
- 📊 **Real-time Data**: Fetches current portfolio value and today's P&L
- 📱 **Multi-Provider SMS**: Supports Twilio, MSG91, and Fast2SMS
- ⏰ **Scheduled Notifications**: Daily updates at market close (3:30 PM IST)
- 🔒 **Environment Variables**: Secure credential management

## Quick Start

### 1. Installation

```bash
cd portfolio_notifier
pip install -r requirements.txt
```

### 2. Configuration

Copy the example environment file and add your credentials:

```bash
cp .env.example .env
```

Edit `.env` with your details:

```env
# Groww Credentials
GROWW_EMAIL=your_email@example.com
GROWW_PASSWORD=your_password
GROWW_PIN=your_pin  # Optional, if required

# Mobile Number (with country code)
MOBILE_NUMBER=+919876543210

# SMS Provider (choose one: twilio, msg91, fast2sms)
SMS_PROVIDER=twilio

# Twilio Credentials (if using Twilio)
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=+1234567890
```

### 3. SMS Provider Setup

Choose one of the following providers:

#### Option A: Twilio (Recommended for testing)
1. Sign up at [twilio.com](https://www.twilio.com/)
2. Get free trial credits
3. Note your Account SID, Auth Token, and Phone Number
4. Set `SMS_PROVIDER=twilio` in `.env`

#### Option B: MSG91 (Indian provider)
1. Sign up at [msg91.com](https://msg91.com/)
2. Get your API key from dashboard
3. Set `SMS_PROVIDER=msg91` in `.env`

#### Option C: Fast2SMS (Indian provider)
1. Sign up at [fast2sms.com](https://www.fast2sms.com/)
2. Get your API key
3. Set `SMS_PROVIDER=fast2sms` in `.env`

## Usage

### Test SMS Sending

```bash
python sms_sender.py
```

This will send a test SMS to verify your configuration.

### Test Portfolio Fetching (Dry Run)

```bash
python portfolio_notifier.py --dry-run --visible
```

- `--dry-run`: Fetches data but doesn't send SMS
- `--visible`: Shows browser window (helpful for debugging)

### Send Actual Notification

```bash
python portfolio_notifier.py --send
```

This will fetch your portfolio data and send SMS notification.

### Run Scheduler (Daily Automation)

```bash
python scheduler.py
```

This will:
- Run continuously in the background
- Send notifications daily at 3:30 PM IST (market close)
- Log all activities to `portfolio_notifier.log`

To test scheduler immediately:
```bash
python scheduler.py --now
```

## Notification Format

You'll receive SMS messages like:

```
📈 ✅ Groww Portfolio Update

TODAY'S GAIN:
₹2,450.75 (+1.85%)

CURRENT VALUE:
₹1,34,892.50

Time: 03:30 PM, 29 Jan 2026
```

## Running as Background Service

### On macOS/Linux (using nohup)

```bash
nohup python scheduler.py > scheduler.out 2>&1 &
```

To stop:
```bash
ps aux | grep scheduler.py
kill <process_id>
```

### On macOS (using launchd)

Create file `~/Library/LaunchAgents/com.portfolio.notifier.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.portfolio.notifier</string>
    <key>ProgramArguments</key>
    <array>
        <string>/Users/rohitkushah/Documents/GitHub/python_-codes_-and_projects/.venv/bin/python</string>
        <string>/Users/rohitkushah/Documents/GitHub/python_-codes_-and_projects/portfolio_notifier/scheduler.py</string>
    </array>
    <key>WorkingDirectory</key>
    <string>/Users/rohitkushah/Documents/GitHub/python_-codes_-and_projects/portfolio_notifier</string>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/tmp/portfolio_notifier.out</string>
    <key>StandardErrorPath</key>
    <string>/tmp/portfolio_notifier.err</string>
</dict>
</plist>
```

Then:
```bash
launchctl load ~/Library/LaunchAgents/com.portfolio.notifier.plist
launchctl start com.portfolio.notifier
```

## Troubleshooting

### Login Issues
- Ensure credentials in `.env` are correct
- Groww may block automated logins - try with `--visible` flag to see what's happening
- Check `screenshots/` folder for debugging screenshots

### SMS Not Received
- Verify mobile number format includes country code (e.g., +91)
- Check SMS provider credits/balance
- Run `python sms_sender.py` to test independently
- Check provider dashboard for delivery status

### Browser/Selenium Issues
- Ensure Chrome is installed
- ChromeDriver is automatically managed by `webdriver-manager`
- Try running with `--visible` to see browser actions

### Screenshots
All screenshots are saved to `screenshots/` directory with timestamps for debugging.

## File Structure

```
portfolio_notifier/
├── portfolio_notifier.py   # Main orchestration
├── groww_fetcher.py        # Groww data fetching
├── sms_sender.py           # SMS notifications
├── scheduler.py            # Daily automation
├── requirements.txt        # Dependencies
├── .env.example           # Configuration template
├── .env                   # Your credentials (gitignored)
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Security Notes

- Never commit `.env` file to version control
- Keep your API credentials secure
- Use environment variables for sensitive data
- SMS providers may charge for messages after free tier

## Customization

### Change Notification Time

Edit `scheduler.py`:
```python
schedule_time = "15:30"  # Change to your preferred time (24-hour format)
```

### Custom Message Format

Edit `portfolio_notifier.py` in the `format_notification_message()` method.

## Support

For issues or questions:
1. Check logs in `portfolio_notifier.log`
2. Review screenshots in `screenshots/` folder
3. Run with `--visible` flag to see browser actions
4. Test components individually (SMS, portfolio fetching)

## License

This project is for personal use. Please respect Groww's terms of service and avoid excessive automated requests.
