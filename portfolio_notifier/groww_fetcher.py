"""
Groww Portfolio Fetcher
Fetches portfolio data from Groww using web scraping with Selenium
"""

import os
import time
from datetime import datetime
from typing import Dict, Optional
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class GrowwPortfolioFetcher:
    """Fetch portfolio data from Groww using web automation"""
    
    def __init__(self, headless: bool = True):
        """
        Initialize the portfolio fetcher
        
        Args:
            headless: Run browser in headless mode (no GUI)
        """
        self.email = os.getenv('GROWW_EMAIL')
        self.password = os.getenv('GROWW_PASSWORD')
        self.pin = os.getenv('GROWW_PIN')
        
        if not all([self.email, self.password]):
            raise ValueError("GROWW_EMAIL and GROWW_PASSWORD must be set in .env file")
        
        self.headless = headless
        self.driver = None
        self.portfolio_data = {}
    
    def _setup_driver(self):
        """Set up Chrome WebDriver with options"""
        chrome_options = Options()
        
        if self.headless:
            chrome_options.add_argument('--headless=new')
        
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # User agent to avoid detection
        chrome_options.add_argument(
            'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Override navigator.webdriver flag
        self.driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )
        
        print("✓ Chrome WebDriver initialized")
    
    def login(self) -> bool:
        """
        Login to Groww account
        
        Returns:
            bool: True if login successful, False otherwise
        """
        try:
            print("🔐 Logging in to Groww...")
            
            # Navigate to Groww login page
            self.driver.get('https://groww.in/login')
            time.sleep(3)
            
            # Wait for email input and enter email
            email_input = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, 'login_email1'))
            )
            email_input.clear()
            email_input.send_keys(self.email)
            print(f"  ✓ Entered email: {self.email}")
            
            # Click continue button
            continue_btn = self.driver.find_element(By.XPATH, '//span[text()="Continue"]')
            continue_btn.click()
            time.sleep(2)
            
            # Wait for password input and enter password
            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'login_password1'))
            )
            password_input.clear()
            password_input.send_keys(self.password)
            print("  ✓ Entered password")
            
            # Click sign in button
            signin_btn = self.driver.find_element(By.XPATH, '//span[text()="Sign In"]')
            signin_btn.click()
            time.sleep(3)
            
            # Check if PIN is required
            if self.pin:
                try:
                    pin_input = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))
                    )
                    pin_input.send_keys(self.pin)
                    print("  ✓ Entered PIN")
                    time.sleep(2)
                except:
                    pass  # PIN not required or already past this step
            
            # Wait for dashboard to load - check for portfolio or user menu
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Portfolio") or contains(text(), "Dashboard")]'))
            )
            
            print("✅ Login successful!")
            return True
            
        except Exception as e:
            print(f"❌ Login failed: {str(e)}")
            self._take_screenshot('login_error')
            return False
    
    def fetch_portfolio_data(self) -> Dict:
        """
        Fetch current portfolio data including today's P&L
        
        Returns:
            dict: Portfolio data with total value, today's gain/loss, etc.
        """
        try:
            print("\n📊 Fetching portfolio data...")
            
            # Navigate to portfolio page
            self.driver.get('https://groww.in/dashboard')
            time.sleep(5)
            
            # Wait for portfolio data to load
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Current Value") or contains(text(), "Total Investment")]'))
            )
            
            portfolio_data = {}
            
            # Try multiple selectors to find portfolio values
            try:
                # Method 1: Look for "Today's Gain" or "Today's Return"
                today_gain_elements = self.driver.find_elements(
                    By.XPATH,
                    '//*[contains(text(), "Today") and (contains(text(), "Gain") or contains(text(), "Return"))]'
                )
                
                if today_gain_elements:
                    parent = today_gain_elements[0].find_element(By.XPATH, '..')
                    gain_text = parent.text
                    portfolio_data['raw_today_gain'] = gain_text
                    print(f"  Found today's data: {gain_text}")
                
                # Method 2: Look for Current Value
                current_value_elements = self.driver.find_elements(
                    By.XPATH,
                    '//*[contains(text(), "Current Value") or contains(text(), "Portfolio Value")]'
                )
                
                if current_value_elements:
                    parent = current_value_elements[0].find_element(By.XPATH, '..')
                    value_text = parent.text
                    portfolio_data['raw_current_value'] = value_text
                    print(f"  Found current value: {value_text}")
                
                # Method 3: Look for Total Returns
                total_return_elements = self.driver.find_elements(
                    By.XPATH,
                    '//*[contains(text(), "Total Returns") or contains(text(), "Overall")]'
                )
                
                if total_return_elements:
                    parent = total_return_elements[0].find_element(By.XPATH, '..')
                    return_text = parent.text
                    portfolio_data['raw_total_return'] = return_text
                    print(f"  Found total returns: {return_text}")
                
            except Exception as e:
                print(f"  ⚠️ Error extracting specific elements: {str(e)}")
            
            # Take screenshot for debugging
            self._take_screenshot('portfolio_data')
            
            # Parse the extracted data
            parsed_data = self._parse_portfolio_data(portfolio_data)
            
            print("\n✅ Portfolio data fetched successfully!")
            return parsed_data
            
        except Exception as e:
            print(f"❌ Failed to fetch portfolio data: {str(e)}")
            self._take_screenshot('fetch_error')
            return {}
    
    def _parse_portfolio_data(self, raw_data: Dict) -> Dict:
        """
        Parse raw portfolio data into structured format
        
        Args:
            raw_data: Raw data extracted from page
            
        Returns:
            dict: Parsed portfolio data
        """
        import re
        
        parsed = {
            'current_value': 0.0,
            'today_gain': 0.0,
            'today_gain_percent': 0.0,
            'total_return': 0.0,
            'total_return_percent': 0.0,
            'timestamp': datetime.now().isoformat()
        }
        
        # Helper function to extract numbers from text
        def extract_amount(text: str) -> float:
            """Extract monetary amount from text"""
            # Remove currency symbols and commas
            clean_text = text.replace('₹', '').replace(',', '').replace('+', '').replace(' ', '')
            # Find numbers (including decimals)
            matches = re.findall(r'-?\d+\.?\d*', clean_text)
            if matches:
                return float(matches[0])
            return 0.0
        
        def extract_percentage(text: str) -> float:
            """Extract percentage from text"""
            matches = re.findall(r'(-?\d+\.?\d*)%', text)
            if matches:
                return float(matches[0])
            return 0.0
        
        # Parse each field
        if 'raw_current_value' in raw_data:
            parsed['current_value'] = extract_amount(raw_data['raw_current_value'])
        
        if 'raw_today_gain' in raw_data:
            text = raw_data['raw_today_gain']
            parsed['today_gain'] = extract_amount(text)
            parsed['today_gain_percent'] = extract_percentage(text)
        
        if 'raw_total_return' in raw_data:
            text = raw_data['raw_total_return']
            parsed['total_return'] = extract_amount(text)
            parsed['total_return_percent'] = extract_percentage(text)
        
        return parsed
    
    def _take_screenshot(self, name: str):
        """Take screenshot for debugging"""
        try:
            os.makedirs('screenshots', exist_ok=True)
            filename = f"screenshots/{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            self.driver.save_screenshot(filename)
            print(f"  📸 Screenshot saved: {filename}")
        except Exception as e:
            print(f"  ⚠️ Could not save screenshot: {str(e)}")
    
    def get_portfolio_summary(self) -> Dict:
        """
        Complete workflow: login and fetch portfolio data
        
        Returns:
            dict: Portfolio summary with all data
        """
        try:
            self._setup_driver()
            
            if not self.login():
                return {'error': 'Login failed'}
            
            time.sleep(3)
            portfolio_data = self.fetch_portfolio_data()
            
            return portfolio_data
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return {'error': str(e)}
        
        finally:
            self.cleanup()
    
    def cleanup(self):
        """Clean up resources"""
        if self.driver:
            print("\n🧹 Cleaning up...")
            self.driver.quit()
            print("✓ Browser closed")


def test_portfolio_fetch():
    """Test portfolio fetching"""
    print("=" * 60)
    print("Testing Groww Portfolio Fetcher")
    print("=" * 60)
    
    fetcher = GrowwPortfolioFetcher(headless=False)  # Set to False to see browser
    data = fetcher.get_portfolio_summary()
    
    print("\n" + "=" * 60)
    print("PORTFOLIO DATA")
    print("=" * 60)
    
    if 'error' in data:
        print(f"❌ Error: {data['error']}")
    else:
        print(f"Current Value: ₹{data.get('current_value', 0):,.2f}")
        print(f"Today's Gain: ₹{data.get('today_gain', 0):+,.2f} ({data.get('today_gain_percent', 0):+.2f}%)")
        print(f"Total Return: ₹{data.get('total_return', 0):+,.2f} ({data.get('total_return_percent', 0):+.2f}%)")
        print(f"Timestamp: {data.get('timestamp', 'N/A')}")
    
    return data


if __name__ == "__main__":
    test_portfolio_fetch()
