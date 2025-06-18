# ticketing-system
A web service for users to purchase electronic tickets to cultural venues (museums, exhibitions, etc.), with an admin panel for managing venues, tickets, and payments, and a QR-code-based entry control system — project name: "culture-ticketing"
# 🎟️ Culture Ticketing System

A full-featured web service for purchasing electronic tickets to cultural venues (museums, exhibitions, galleries, and more). The system includes a user-facing interface, an administrative panel for managing venues and payments, a QR-code-based access control system, and full integration with online payments.

---

## Project Features

### User Portal (Frontend)

- Browse cultural objects by city, category, and price
- View detailed venue pages (description, address, schedule, images)
- Select date/time for visiting
- Purchase tickets online
- Receive electronic tickets with QR-codes (via email and personal dashboard)
- Personal account with order history and downloadable tickets

### Admin Panel

- Role-based access for **Administrators** and **Controllers**
- Full CRUD for cultural venues:
  - Name, description, city, address
  - Working hours
  - Ticket prices and availability per time slot
- Ticket and payment management:
  - View orders by user, date, venue
  - Payment status, ticket QR-code
  - Export reports to CSV/Excel
- Dashboard with statistics:
  - Sales by venue, date, and city
  - Number of visitors
  - Revenue tracking

### QR Code Entry Control

- Web/mobile interface for scanning QR codes
- Real-time validation:
  - Ticket validity
  - Payment status
  - Date/time match
  - Duplicate use detection
- Immediate visual feedback to staff

### Online Payments

- Integrated with payment gateway (e.g. Kaspi Pay, Halyk Pay, Stripe)
- Secure credit/debit card transactions
- Real-time confirmation
- Error handling and logging
- Payment history stored in admin panel

---
## Deployment & Setup

1. **Clone the project**
   ```bash
   git clone https://github.com/yourusername/culture-ticketing.git
   cd culture-ticketing
Setup backend

```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
Setup frontend

```bash
cd ../frontend
npm install
npm run build
Run the project

```bash
# Backend
python manage.py runserver

# Frontend
npm start
Environment Variables
Create a .env file for backend:

DB_URL=postgres://user:password@host:port/db
SECRET_KEY=your-secret
PAYMENT_API_KEY=xxx


