# DriveMatch

A web-based platform that connects passengers with verified monthly drivers in Riyadh, Saudi Arabia. Built with Django as a student-level project.

## Features

- **Passenger**: Register, search drivers, book subscriptions, view contracts, rate drivers, submit complaints
- **Driver**: 7-step registration, dashboard, manage trips/subscribers/earnings/ratings
- **Admin**: Verify drivers, manage bookings/contracts/refunds via Django admin

## Requirements

- Python 3.10+
- Django 5.x
- Pillow (for image uploads)

## Setup

Open terminal (PowerShell on Windows) and run:

```bash
# Install dependencies
python -m pip install Django Pillow

# Navigate to project folder
cd DriveMatch

# Check for issues
python manage.py check

# Create database tables
python manage.py makemigrations accounts
python manage.py makemigrations drivers
python manage.py makemigrations bookings
python manage.py makemigrations support
python manage.py makemigrations main
python manage.py migrate

# Seed subscription plans and Riyadh routes
python manage.py seed_drivematch_data

# Create admin user
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

Then open http://127.0.0.1:8000/ in your browser.

## Admin Setup

1. Go to http://127.0.0.1:8000/admin/
2. The seed command creates 4 subscription plans and all Riyadh routes automatically
3. After a driver registers, approve them in Admin > Driver Profiles > change verification_status to "Approved"

## Testing Checklist

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open http://127.0.0.1:8000/ | Landing page with Register/Sign In buttons |
| 2 | Register as Passenger | Account created, redirected to sign in |
| 3 | Sign in with email + password | Redirected to passenger home |
| 4 | Register as Driver (7 steps) | Account created, pending verification |
| 5 | Admin: Approve driver | Driver appears in search results |
| 6 | Passenger: Search drivers | Verified drivers shown with filters |
| 7 | Passenger: Book a driver | Booking confirmed, contract created |
| 8 | View contract | Full contract with print button |
| 9 | View invoices | Invoice list with amounts |
| 10 | Admin: Set booking to "completed" | Passenger can rate driver |
| 11 | Passenger: Rate driver | Star rating submitted |
| 12 | Passenger: Submit complaint | Complaint created |
| 13 | Driver: Submit cancellation request | Request pending admin review |
| 14 | Admin: Process refund | Refund record created |

## Simulated Features

- **OTP verification**: Simulated as auto-verified on registration
- **Payment**: Simulated — any 4-digit card number accepted
- **PDF contract**: Uses browser print (window.print) instead of PDF library

## Project Structure

```
DriveMatch/
├── manage.py
├── DriveMatch/          (settings, urls)
├── main/                (landing, home, terms, privacy, CSS)
├── accounts/            (passenger registration, sign in, profile)
├── drivers/             (driver registration, dashboard, search)
├── bookings/            (booking, contract, payment, rating, invoice)
└── support/             (contact, tickets, complaints)
```
