# Gmail API Setup Instructions for FEC Daily Reports

## Overview
This guide will help you set up Gmail API authentication to send FEC reports from `aaronkfaver@gmail.com` to `aaron.faver@actx.edu`.

## Prerequisites
- Google account (aaronkfaver@gmail.com)
- Access to Google Cloud Console
- Python 3.x with Gmail API libraries installed

## Step-by-Step Setup

### 1. Google Cloud Console Setup

1. **Go to Google Cloud Console**
   - Visit: https://console.cloud.google.com/
   - Sign in with aaronkfaver@gmail.com

2. **Create or Select Project**
   - Click "Select a project" at the top
   - Either create a new project or select existing one
   - Suggested name: "FEC Daily Reports"

3. **Enable Gmail API**
   - Go to "APIs & Services" > "Library"
   - Search for "Gmail API"
   - Click on "Gmail API" and click "Enable"

### 2. Create OAuth2 Credentials

1. **Go to Credentials**
   - Navigate to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth client ID"

2. **Configure OAuth Consent Screen** (if prompted)
   - Choose "External" user type
   - Fill in required fields:
     - App name: "FEC Daily Reports"
     - User support email: aaronkfaver@gmail.com
     - Developer contact: aaronkfaver@gmail.com
   - Add scope: `https://www.googleapis.com/auth/gmail.send`
   - Add test user: aaronkfaver@gmail.com

3. **Create OAuth Client ID**
   - Application type: "Desktop application"
   - Name: "FEC Reports Desktop Client"
   - Click "Create"

4. **Download Credentials**
   - Click the download button (⬇️) next to your new OAuth client
   - Save the file as `credentials.json`
   - Move this file to: `/Users/ak/Desktop/FEC project NEW/credentials.json`

### 3. Test Gmail API

1. **Run the test script**:
   ```bash
   cd "/Users/ak/Desktop/FEC project NEW"
   python3 gmail_api_sender.py
   ```

2. **Complete OAuth Flow**:
   - A browser window will open
   - Sign in with aaronkfaver@gmail.com
   - Grant permissions to send emails
   - The browser will show "The authentication flow has completed"

3. **Verify Test Email**:
   - Check aaron.faver@actx.edu inbox
   - Look for "FEC Gmail API Test" email

### 4. Update FEC System

The FEC system will automatically use Gmail API once credentials are set up.

## File Structure
After setup, you should have:
```
/Users/ak/Desktop/FEC project NEW/
├── credentials.json          # OAuth2 credentials (from Google Cloud)
├── token.json               # Auto-generated after first auth
├── gmail_api_sender.py      # Gmail API email sender
├── fec_enhanced_final.py    # Main FEC system
└── .env                     # Environment variables
```

## Configuration Details

### Email Settings
- **From**: aaronkfaver@gmail.com
- **To**: aaron.faver@actx.edu
- **Method**: Gmail API with OAuth2
- **Scope**: Send emails only

### Security Notes
- OAuth2 is more secure than app passwords
- Credentials are stored locally and encrypted
- No passwords stored in plain text
- Tokens automatically refresh

## Troubleshooting

### Common Issues

1. **"credentials.json not found"**
   - Download credentials from Google Cloud Console
   - Place in correct directory

2. **"Access blocked"**
   - Ensure OAuth consent screen is configured
   - Add aaronkfaver@gmail.com as test user

3. **"Scope not authorized"**
   - Check OAuth consent screen scopes
   - Ensure gmail.send scope is added

4. **Browser doesn't open**
   - Run script from terminal
   - Check firewall settings

### Testing Commands

```bash
# Test Gmail API
python3 gmail_api_sender.py

# Test full FEC system with Gmail
python3 fec_enhanced_final.py

# Check credentials
ls -la credentials.json token.json
```

## Success Indicators

✅ **Setup Complete When**:
- credentials.json exists
- token.json created after first auth
- Test email received at aaron.faver@actx.edu
- FEC system sends emails without errors

## Next Steps

After successful setup:
1. Gmail API will be used automatically
2. Daily reports will be sent to aaron.faver@actx.edu
3. No further configuration needed
4. Tokens refresh automatically

## Support

If you encounter issues:
1. Check Google Cloud Console for API quotas
2. Verify OAuth consent screen configuration
3. Ensure correct email addresses are used
4. Run test script to isolate issues

---

**Generated**: October 12, 2025
**System**: FEC Enhanced Automation System
