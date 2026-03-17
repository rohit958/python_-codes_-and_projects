"""
Scheduler for Portfolio Notifier
Runs the portfolio notifier at specified times daily
"""

import schedule
import time
import logging
from datetime import datetime
from portfolio_notifier import PortfolioNotifier

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('portfolio_notifier.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def send_notification():
    """Job function to send portfolio notification"""
    logger.info("=" * 70)
    logger.info("Starting scheduled portfolio notification")
    logger.info("=" * 70)
    
    try:
        notifier = PortfolioNotifier(dry_run=False)
        result = notifier.run(headless=True)
        
        if result.get('success'):
            logger.info("✅ Portfolio notification sent successfully")
            
            # Log portfolio details
            portfolio = result.get('portfolio_data', {})
            logger.info(f"Current Value: ₹{portfolio.get('current_value', 0):,.2f}")
            logger.info(f"Today's Gain/Loss: ₹{portfolio.get('today_gain', 0):+,.2f}")
            
            # Log notification details
            notification = result.get('notification', {})
            if notification.get('success'):
                logger.info(f"SMS sent - Message ID: {notification.get('message_id', 'N/A')}")
        else:
            logger.error("❌ Portfolio notification failed")
            if 'error' in result:
                logger.error(f"Error: {result['error']}")
            
    except Exception as e:
        logger.error(f"❌ Critical error in scheduled job: {str(e)}", exc_info=True)


def run_scheduler():
    """Run the scheduler continuously"""
    
    # Schedule the notification
    # Default: Run at market close time (3:30 PM IST)
    schedule_time = "15:30"
    
    schedule.every().day.at(schedule_time).do(send_notification)
    
    logger.info("")
    logger.info("=" * 70)
    logger.info(" " * 20 + "PORTFOLIO NOTIFIER SCHEDULER")
    logger.info("=" * 70)
    logger.info(f"Scheduled Time: {schedule_time} (3:30 PM IST)")
    logger.info(f"Current Time: {datetime.now().strftime('%H:%M:%S')}")
    logger.info(f"Next Run: {schedule.next_run()}")
    logger.info("")
    logger.info("Press Ctrl+C to stop the scheduler")
    logger.info("=" * 70)
    logger.info("")
    
    # Keep the script running
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
            
    except KeyboardInterrupt:
        logger.info("\n\n👋 Scheduler stopped by user")
        logger.info("=" * 70)


if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║            GROWW PORTFOLIO NOTIFIER - SCHEDULER                  ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

This scheduler will automatically send portfolio updates to your
mobile number every day at market close (3:30 PM IST).

Logs are saved to: portfolio_notifier.log
""")
    
    # Option to run immediately for testing
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == '--now':
        logger.info("Running immediate test notification...")
        send_notification()
        sys.exit(0)
    
    # Start the scheduler
    run_scheduler()
