import random
import smtplib


def generate_otp() -> int:
    """Generate 6-digit OTP"""
    return random.randint(100000, 999999)


def send_email_otp(receiver_email: str, otp: int) -> None:
    """Send OTP to email"""

    sender_email = "aniketpawarpatil2020@gmail.com"
    sender_password = "zdlc ktqd cvqo bmpd"  # Gmail App Password

    message = f"Subject: Email OTP Verification\n\nYour OTP is: {otp}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)
        server.quit()
        print("📧 OTP sent successfully!")
    except smtplib.SMTPException as e:
        print("❌ Failed to send OTP")
        print(e)


def main():
    email = input("Enter email address: ").strip()

    generated_otp = generate_otp()
    send_email_otp(email, generated_otp)

    user_otp = int(input("Enter OTP received on email: "))

    if user_otp == generated_otp:
        print("✅ OTP Verified Successfully!")
    else:
        print("❌ Invalid OTP. Verification Failed.")


if __name__ == "__main__":
    main()
