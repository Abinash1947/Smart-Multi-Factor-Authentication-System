#  FaceSecure – Multi-Factor Authentication System

A secure login system that combines **User ID, Password, OTP Verification, and Face Authentication** to provide multi-factor user authentication.

##  1. Introduction

Traditional login systems generally depend only on a username and password. If the password is stolen, an unauthorized person may gain access to the account.

**FaceSecure** improves login security by adding multiple verification layers. A user must successfully complete the required authentication steps before access is granted.

The system uses:

* User ID
* Password
* OTP Verification
* Face Authentication

##  2. Objectives

The main objectives of this project are:

* To develop a secure multi-factor login system.
* To combine knowledge-based and biometric authentication.
* To verify users using OTP.
* To verify the user's identity using facial recognition.
* To reduce the risk of unauthorized account access.
* To demonstrate practical implementation of MFA.

##  3. Key Features

* User ID verification
* Password authentication
* OTP-based verification
* Face recognition
* Multi-factor authentication
* Secure login workflow
* Authentication success/failure messages
* Simple and user-friendly login interface

##  4. Authentication Factors

### Factor 1 – User ID and Password

The user enters their registered User ID and password.

```text
User ID + Password
        ↓
   Credential Check
```

### Factor 2 – OTP

After successful credential verification, an OTP is generated and sent to the registered communication channel.

```text
OTP Generated
      ↓
OTP Sent to User
      ↓
User Enters OTP
      ↓
OTP Verification
```

### Factor 3 – Face Authentication

The user then provides a face image through the camera.

The system compares the captured face with the registered face.

```text
Camera
   ↓
Capture Face
   ↓
Face Detection
   ↓
Face Recognition
   ↓
Identity Verification
```

##  5. Complete Authentication Flow

```text
                START
                  ↓
          Enter User ID
                  ↓
          Enter Password
                  ↓
       ┌──────────────────┐
       │ Credentials Valid?│
       └────────┬─────────┘
                │
          Yes   │   No
           ↓    │    ↓
       Generate OTP   Login Failed
           ↓
       Enter OTP
           ↓
       ┌───────────────┐
       │    OTP Valid? │
       └───────┬───────┘
               │
         Yes   │   No
          ↓    │    ↓
    Face Authentication
          ↓
     Capture Face
          ↓
    Compare Face
          ↓
    ┌─────────────────┐
    │ Face Matched?   │
    └────────┬────────┘
             │
       Yes   │   No
        ↓    │    ↓
   ACCESS GRANTED
             │
        Authentication
            Failed
```

##  6. Technologies Used

* **Python**
* **Flask**
* **OpenCV**
* **face_recognition**
* **HTML5**
* **CSS3**
* **JavaScript**
* **OTP Authentication**

##  7. Suggested Project Structure

```text
FaceSecure-MFA/
│
├── app.py
├── face_auth.py
├── otp.py
├── requirements.txt
├── README.md
├── SECURITY.md
│
├── templates/
│   ├── login.html
│   ├── otp.html
│   └── face_auth.html
│
├── static/
│   ├── css/
│   └── js/
│
└── faces/
    └── registered_faces/
```

##  8. How the System Works

### Step 1 – User Login

The user enters their registered User ID and password.

### Step 2 – Credential Verification

The system checks whether the entered credentials are valid.

If the credentials are incorrect, authentication is stopped.

### Step 3 – OTP Verification

If the credentials are correct, an OTP is generated.

The user enters the OTP into the verification page.

If the OTP is incorrect or expired, access is denied.

### Step 4 – Face Authentication

After successful OTP verification, the system activates face authentication.

The user's face is captured using a camera and compared against the registered face.

### Step 5 – Access

If all authentication stages are successful:

```text
User ID ✓
Password ✓
OTP ✓
Face ✓

       ↓

ACCESS GRANTED
```

If any required stage fails:

```text
ACCESS DENIED
```

##  9. Security Features

The project provides multiple security layers:

* Password-based authentication
* Time-sensitive OTP verification
* Biometric face verification
* Multiple authentication stages
* Restricted access after failed verification

### Security Recommendation

Real biometric data should be handled carefully. Do not upload real users' face images, passwords, OTP secrets, or other private information to a public GitHub repository.

## 10. Testing

The system should be tested with:

### Test Case 1 – Correct Credentials

```text
User ID     → Correct
Password    → Correct
OTP         → Correct
Face        → Match

Result → Access Granted
```

### Test Case 2 – Wrong Password

```text
User ID     → Correct
Password    → Incorrect

Result → Access Denied
```

### Test Case 3 – Wrong OTP

```text
Credentials → Correct
OTP         → Incorrect

Result → Access Denied
```

### Test Case 4 – Wrong Face

```text
Credentials → Correct
OTP         → Correct
Face        → Not Matched

Result → Access Denied
```

## 11. Advantages

* Provides stronger authentication than password-only login.
* Combines different authentication factors.
* OTP provides an additional temporary verification layer.
* Face authentication provides biometric verification.
* Can be used as a foundation for secure applications.

## 12. Limitations

* Requires access to a camera for face authentication.
* OTP delivery depends on the configured communication service.
* Face recognition can be affected by lighting and camera quality.
* Biometric information requires careful privacy protection.
* Basic implementations may require additional anti-spoofing protection.

##13. Future Scope

The project can be improved by adding:

* Face liveness detection
* Email/SMS OTP integration
* QR-code authentication
* Fingerprint authentication
* Login attempt limits
* Account lockout
* Database integration
* Admin dashboard
* Authentication logs
* JWT/session security
* HTTPS
* Encrypted biometric storage
* Two-factor or adaptive authentication

## 14. Learning Outcomes

This project provides practical knowledge of:

* Multi-Factor Authentication
* Password authentication
* OTP verification
* Facial recognition
* Computer vision
* Flask web development
* Authentication workflows
* Basic cybersecurity concepts

## 15. Important Security Notes

**Never upload the following to a public repository:**

```text
Passwords
OTP secrets
API keys
.env files
Private keys
Real user face images
Personal user information
```

Use `.gitignore` to prevent sensitive files from being committed.

Example:

```gitignore
__pycache__/
.venv/
.idea/
.env
*.key
*.pem
faces/*
```

## 16. Author

**Abinash Behera**

B.Tech – Computer Science & Engineering

## ⭐ 17. Conclusion

**FaceSecure – Multi-Factor Authentication System** demonstrates how multiple authentication mechanisms can be combined to create a stronger login process.

By requiring **User ID + Password + OTP + Face Authentication**, the system provides multiple layers of identity verification and demonstrates the practical application of cybersecurity and biometric authentication.
