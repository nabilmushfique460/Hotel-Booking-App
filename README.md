# 🏨 Object-Oriented Hotel Booking & Reservation System (Python)

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Architecture: OOP](https://img.shields.io/badge/Architecture-Object--Oriented-orange?style=for-the-badge)](#)
[![Data: Pandas](https://img.shields.io/badge/Data-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)

A modular, clean Object-Oriented Programming (OOP) reservation and transaction validation engine built in Python. Features real-time room availability tracking, card security validation, and automated digital booking ticket generation.

---

## 🏛️ Domain Architecture & OOP Design

The core system utilizes clean OOP design patterns:

- **`Hotel`**: Encapsulates hotel properties (ID, name, city, price) and manages dynamic availability state in persistent storage (`hotels.csv`).
- **`CreditCard`**: Validates cardholder identity, card number, expiration dates, and security CVC checksums against merchant records (`cards.csv`).
- **`SecureCreditcard (Inherits CreditCard)`**: Extends standard card verification with secondary two-factor authentication and encrypted PIN/password matching (`card-security.csv`).
- **`ReservationTicket`**: Constructs formatted confirmation tickets upon authorized settlement.

---

## 🚀 Getting Started

### 1. Installation
```bash
git clone https://github.com/nabilmushfique460/Hotel-Booking-App.git
cd Hotel-Booking-App
pip install -r requirements.txt
```

### 2. Run the Booking Engine
```bash
python main.py
```

Follow the interactive terminal prompts:
1. Review available hotels and select a `hotel_id`.
2. Input customer information and demo payment credentials.
3. Authenticate with the secure password to complete the reservation and receive an instant booking ticket!

---

## 💼 Custom Software & Booking System Inquiries
Looking to build custom booking portals, reservation engines, or payment processing workflows?

- **Developer:** S.M. Nabil Mushfique
- **Email:** [nabilmushfique460@gmail.com](mailto:nabilmushfique460@gmail.com)
- **Services:** Full-stack Web Apps (Django/Flask/React), OOP System Architecture, Database & API Integrations.
