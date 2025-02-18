from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# ✅ Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Open Chrome in full screen
options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass bot detection

# ✅ Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# ✅ Open DexScreener directly
print("🚀 Opening DexScreener...")
driver.get("https://dexscreener.com/solana")

# ✅ Wait for the page to load
time.sleep(5)

# ✅ Click on the first token in the table
try:
    print("📊 Finding the first token in the list...")

    # ✅ Find all tokens in the table
    token_rows = driver.find_elements(By.CSS_SELECTOR, "a.ds-dex-table-row.ds-dex-table-row-top")

    if not token_rows:
        print("❌ No tokens found!")
        driver.quit()
        exit()

    # ✅ Select the first token dynamically
    first_token = token_rows[0]

    # ✅ Extract Token Name & Pair
    try:
        token_name = first_token.find_element(By.CSS_SELECTOR, "span.chakra-text.ds-dex-table-row-base-token-symbol").text
        token_pair = first_token.find_element(By.CSS_SELECTOR, "span.ds-dex-table-row-quote-token-symbol").text
        print(f"✅ Successfully found the first token: {token_name}/{token_pair}")
    except Exception as e:
        print("❌ Error extracting token details:", e)

    # ✅ Extract Token Page Link
    token_link = first_token.get_attribute("href")
    print(f"🔗 Token Page Link: {token_link}")

    # ✅ Click on the token to navigate
    first_token.click()
    print("🚀 Navigating to token page...")

    # ✅ Wait for the token page to load
    time.sleep(5)

    # ✅ Extract Twitter & Telegram Links
    try:
        twitter_link = driver.find_element(By.XPATH, "//button[contains(@class, 'chakra-button') and contains(@href, 'x.com')]").get_attribute("href")
    except:
        twitter_link = "❌ No Twitter link found"

    try:
        telegram_link = driver.find_element(By.XPATH, "//button[contains(@class, 'chakra-button') and contains(@href, 't.me')]").get_attribute("href")
    except:
        telegram_link = "❌ No Telegram link found"

    print(f"\n🐦 Twitter: {twitter_link}")
    print(f"📢 Telegram: {telegram_link}")

except Exception as e:
    print("❌ Error:", e)

# ✅ Keep browser open for 30 seconds for review, then close
time.sleep(30)
driver.quit()
