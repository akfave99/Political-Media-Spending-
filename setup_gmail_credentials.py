#!/usr/bin/env python3
"""
Gmail API Credentials Setup Helper

This script helps set up Gmail API credentials for the FEC Daily Report system.
It provides step-by-step guidance and validates the setup.
"""

import os
import json
from datetime import datetime

def check_credentials_file():
    """Check if credentials.json exists"""
    if os.path.exists('credentials.json'):
        print("✅ credentials.json found")
        try:
            with open('credentials.json', 'r') as f:
                creds = json.load(f)
            
            if 'installed' in creds:
                client_id = creds['installed'].get('client_id', 'Unknown')
                print(f"📋 Client ID: {client_id[:20]}...")
                return True
            else:
                print("⚠️ credentials.json format may be incorrect")
                return False
        except Exception as e:
            print(f"❌ Error reading credentials.json: {e}")
            return False
    else:
        print("❌ credentials.json not found")
        return False

def check_token_file():
    """Check if token.json exists"""
    if os.path.exists('token.json'):
        print("✅ token.json found (authentication completed)")
        return True
    else:
        print("⚠️ token.json not found (authentication needed)")
        return False

def create_sample_credentials():
    """Create a sample credentials.json template"""
    sample_creds = {
        "installed": {
            "client_id": "YOUR_CLIENT_ID.apps.googleusercontent.com",
            "project_id": "your-project-id",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": "YOUR_CLIENT_SECRET",
            "redirect_uris": ["http://localhost"]
        }
    }
    
    with open('credentials_template.json', 'w') as f:
        json.dump(sample_creds, f, indent=2)
    
    print("📝 Created credentials_template.json as reference")

def provide_setup_instructions():
    """Provide detailed setup instructions"""
    print("\n" + "="*60)
    print("📋 GMAIL API SETUP INSTRUCTIONS")
    print("="*60)
    
    print("""
🎯 QUICK SETUP STEPS:

1. Go to Google Cloud Console:
   https://console.cloud.google.com/

2. Create/Select Project:
   - Click "Select a project"
   - Create new project: "FEC Daily Reports"

3. Enable Gmail API:
   - Go to "APIs & Services" > "Library"
   - Search "Gmail API" and enable it

4. Create OAuth2 Credentials:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth client ID"
   - Application type: "Desktop application"
   - Name: "FEC Reports Desktop Client"

5. Download Credentials:
   - Click download button (⬇️)
   - Save as "credentials.json" in this directory

6. Test Setup:
   python3 gmail_api_sender.py

📧 EMAIL CONFIGURATION:
   From: aaronkfaver@gmail.com
   To: aaron.faver@actx.edu

🔧 CURRENT STATUS:""")
    
    creds_ok = check_credentials_file()
    token_ok = check_token_file()
    
    if creds_ok and token_ok:
        print("   ✅ READY: Gmail API fully configured")
    elif creds_ok and not token_ok:
        print("   🔄 NEEDS AUTH: Run 'python3 gmail_api_sender.py' to authenticate")
    else:
        print("   ❌ NEEDS SETUP: Follow steps above to create credentials.json")

def main():
    """Main setup function"""
    print("🔧 Gmail API Credentials Setup Helper")
    print("="*50)
    
    print(f"📁 Current directory: {os.getcwd()}")
    print(f"🕐 Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    print("\n🔍 Checking current setup...")
    
    creds_exists = check_credentials_file()
    token_exists = check_token_file()
    
    if creds_exists and token_exists:
        print("\n🎉 Gmail API is fully configured!")
        print("✅ Ready to send FEC reports")
        
        # Test the configuration
        print("\n🧪 Testing Gmail API...")
        try:
            from gmail_api_sender import test_gmail_api
            test_gmail_api()
        except Exception as e:
            print(f"❌ Test failed: {e}")
    
    elif creds_exists and not token_exists:
        print("\n🔄 Credentials found, authentication needed")
        print("Run: python3 gmail_api_sender.py")
    
    else:
        print("\n❌ Setup required")
        create_sample_credentials()
        provide_setup_instructions()

if __name__ == "__main__":
    main()
