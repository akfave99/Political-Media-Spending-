#!/usr/bin/env python3
"""
Gmail API Email Sender for FEC Daily Reports

This module provides Gmail API functionality to send FEC reports via email.
Uses OAuth2 authentication for secure, reliable email delivery.

Configuration:
- Send from: aaronkfaver@gmail.com
- Send to: aaron.faver@actx.edu
- Supports attachments and HTML emails
"""

import os
import base64
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import mimetypes
from datetime import datetime

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    GMAIL_API_AVAILABLE = True
except ImportError:
    GMAIL_API_AVAILABLE = False

class GmailAPISender:
    """Gmail API email sender for FEC reports"""
    
    # Gmail API scope for sending emails
    SCOPES = ['https://www.googleapis.com/auth/gmail.send']
    
    def __init__(self):
        """Initialize Gmail API sender"""
        self.service = None
        self.credentials_file = 'credentials.json'
        self.token_file = 'token.json'
        
        # Email configuration
        self.sender_email = 'aaronkfaver@gmail.com'
        self.recipient_email = 'aaron.faver@actx.edu'
        
        print("📧 Initializing Gmail API Email Sender...")
        
        if not GMAIL_API_AVAILABLE:
            raise ImportError("Gmail API libraries not available. Run: pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client")
    
    def authenticate(self):
        """Authenticate with Gmail API using OAuth2"""
        creds = None
        
        # Load existing token
        if os.path.exists(self.token_file):
            creds = Credentials.from_authorized_user_file(self.token_file, self.SCOPES)
        
        # If no valid credentials, get new ones
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                try:
                    creds.refresh(Request())
                    print("✅ Refreshed existing Gmail API credentials")
                except Exception as e:
                    print(f"⚠️ Failed to refresh credentials: {e}")
                    creds = None
            
            if not creds:
                if not os.path.exists(self.credentials_file):
                    raise FileNotFoundError(f"""
❌ Gmail API credentials file not found: {self.credentials_file}

📋 SETUP REQUIRED:
1. Go to https://console.cloud.google.com/
2. Create a new project or select existing project
3. Enable Gmail API
4. Create OAuth2 credentials (Desktop application)
5. Download credentials.json to this directory
6. Run this script again

See GMAIL_API_SETUP_INSTRUCTIONS.md for detailed steps.
""")
                
                flow = InstalledAppFlow.from_client_secrets_file(self.credentials_file, self.SCOPES)
                creds = flow.run_local_server(port=0)
                print("✅ Completed Gmail API authentication")
            
            # Save credentials for next run
            with open(self.token_file, 'w') as token:
                token.write(creds.to_json())
        
        # Build Gmail service
        self.service = build('gmail', 'v1', credentials=creds)
        print("✅ Gmail API service initialized")
        return True
    
    def create_message(self, subject, body, attachment_paths=None):
        """Create email message with optional multiple attachments"""
        message = MIMEMultipart()
        message['to'] = self.recipient_email
        message['from'] = self.sender_email
        message['subject'] = subject

        # Add body
        message.attach(MIMEText(body, 'html'))

        # Add attachments if provided
        if attachment_paths:
            # Handle single attachment path (backward compatibility)
            if isinstance(attachment_paths, str):
                attachment_paths = [attachment_paths]

            for attachment_path in attachment_paths:
                if attachment_path and os.path.exists(attachment_path):
                    content_type, encoding = mimetypes.guess_type(attachment_path)

                    if content_type is None or encoding is not None:
                        content_type = 'application/octet-stream'

                    main_type, sub_type = content_type.split('/', 1)

                    with open(attachment_path, 'rb') as fp:
                        attachment = MIMEBase(main_type, sub_type)
                        attachment.set_payload(fp.read())

                    encoders.encode_base64(attachment)
                    filename = os.path.basename(attachment_path)
                    attachment.add_header('Content-Disposition', f'attachment; filename="{filename}"')
                    message.attach(attachment)

                    print(f"📎 Attached file: {filename}")
                else:
                    print(f"⚠️ Attachment not found: {attachment_path}")

        # Encode message
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
        return {'raw': raw_message}
    
    def send_email(self, subject, body, attachment_paths=None):
        """Send email via Gmail API with multiple attachments support"""
        try:
            if not self.service:
                self.authenticate()

            message = self.create_message(subject, body, attachment_paths)

            result = self.service.users().messages().send(
                userId='me',
                body=message
            ).execute()

            print(f"✅ Email sent successfully!")
            print(f"📧 From: {self.sender_email}")
            print(f"📧 To: {self.recipient_email}")
            print(f"📋 Subject: {subject}")
            print(f"📨 Message ID: {result['id']}")

            return True

        except HttpError as error:
            print(f"❌ Gmail API error: {error}")
            return False
        except Exception as error:
            print(f"❌ Email sending failed: {error}")
            return False

    def find_csv_files(self, base_timestamp=None):
        """Find CSV files generated for the current report"""
        import glob

        csv_files = []

        if base_timestamp:
            # Look for CSV files with the specific timestamp
            pattern = f"FEC_*_{base_timestamp}.csv"
        else:
            # Look for the most recent CSV files
            pattern = "FEC_*.csv"

        found_files = glob.glob(pattern)

        # Sort by modification time (newest first)
        found_files.sort(key=os.path.getmtime, reverse=True)

        # If we have a timestamp, get all files with that timestamp
        if base_timestamp:
            csv_files = [f for f in found_files if base_timestamp in f]
        else:
            # Get the most recent set of CSV files (same timestamp)
            if found_files:
                # Extract timestamp from the first file
                import re
                match = re.search(r'_(\d{8}_\d{6})\.csv$', found_files[0])
                if match:
                    timestamp = match.group(1)
                    csv_files = [f for f in found_files if timestamp in f]

        return csv_files

    def send_fec_report(self, report_path, report_date=None, include_csv=True):
        """Send FEC report via Gmail API with optional CSV files"""
        if not report_date:
            report_date = datetime.now().strftime("%Y-%m-%d")

        # Prepare attachments list
        attachments = [report_path]

        # Find and include CSV files if requested
        csv_files = []
        if include_csv:
            csv_files = self.find_csv_files()
            attachments.extend(csv_files)
            print(f"📊 Found {len(csv_files)} CSV files to attach")

        subject = f"FEC Daily Report - {report_date}"

        # Update body to mention CSV files
        csv_section = ""
        if csv_files:
            csv_section = f"""
        <h3>📄 CSV Data Files Included:</h3>
        <ul>
            <li>Republicans Data (CSV)</li>
            <li>Democrats Data (CSV)</li>
            <li>Committee Analysis (CSV)</li>
            <li>Geographic Analysis (CSV)</li>
            <li>PVI Analysis (CSV)</li>
            <li>Political Metrics (CSV)</li>
        </ul>
        <p><em>CSV files provide raw data for further analysis and processing.</em></p>
        """

        body = f"""
        <html>
        <body>
        <h2>🏛️ FEC Daily Congressional Analysis Report</h2>
        <p><strong>Report Date:</strong> {report_date}</p>
        <p><strong>Generated:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>

        <h3>📊 Excel Report Contents:</h3>
        <ul>
            <li>Executive Summary</li>
            <li>Top Republican Fundraisers</li>
            <li>Top Democratic Fundraisers</li>
            <li>PVI Analysis</li>
            <li>Committee Analysis</li>
            <li>Geographic Analysis</li>
            <li>GIS Visualization</li>
            <li>Advanced Charts</li>
            <li>Political Metrics</li>
            <li>Methodology</li>
        </ul>
        {csv_section}
        <h3>🔧 System Information:</h3>
        <ul>
            <li><strong>System:</strong> FEC Enhanced Final System</li>
            <li><strong>Email Method:</strong> Gmail API</li>
            <li><strong>Automation:</strong> Daily at 7:00 AM (Weekdays)</li>
            <li><strong>Data Source:</strong> FEC API (2026 Election Cycle)</li>
            <li><strong>Attachments:</strong> {len(attachments)} files (Excel + CSV)</li>
        </ul>

        <p>This automated report provides comprehensive analysis of congressional campaign finance data in both Excel and CSV formats.</p>

        <hr>
        <p><em>Generated by FEC Enhanced Automation System</em></p>
        </body>
        </html>
        """

        return self.send_email(subject, body, attachments)

def test_gmail_api():
    """Test Gmail API functionality"""
    print("🧪 Testing Gmail API Email Sender...")
    
    try:
        sender = GmailAPISender()
        
        # Test basic email
        test_subject = "FEC Gmail API Test - " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        test_body = """
        <html>
        <body>
        <h2>✅ Gmail API Test Successful!</h2>
        <p>This email confirms that the Gmail API is working correctly for the FEC Daily Report system.</p>
        
        <h3>Configuration:</h3>
        <ul>
            <li><strong>From:</strong> aaronkfaver@gmail.com</li>
            <li><strong>To:</strong> aaron.faver@actx.edu</li>
            <li><strong>Method:</strong> Gmail API with OAuth2</li>
            <li><strong>Status:</strong> ACTIVE</li>
        </ul>
        
        <p>The FEC system is now ready to send automated daily reports!</p>
        
        <hr>
        <p><em>FEC Enhanced Automation System</em></p>
        </body>
        </html>
        """
        
        success = sender.send_email(test_subject, test_body)
        
        if success:
            print("🎉 Gmail API test completed successfully!")
            print("📧 Check aaron.faver@actx.edu for the test email")
            return True
        else:
            print("❌ Gmail API test failed")
            return False
            
    except Exception as e:
        print(f"❌ Gmail API test error: {e}")
        return False

if __name__ == "__main__":
    test_gmail_api()
