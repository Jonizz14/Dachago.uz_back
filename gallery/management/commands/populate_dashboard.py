import random
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from gallery.models import (
    Product, Booking, Review, Activity,
    Employee, Payment, Service, Announcement, Settings
)

class Command(BaseCommand):
    help = 'Populate dashboard with sample data'

    def handle(self, *args, **options):
        # 0. Clear existing data to avoid unique constraints
        Booking.objects.all().delete()
        Review.objects.all().delete()
        Activity.objects.all().delete()
        Employee.objects.all().delete()
        Payment.objects.all().delete()
        Announcement.objects.all().delete()

        # 1. Update some Product categories and status
        products = Product.objects.all()
        categories = ['Mountain', 'Villa', 'Lake', 'Cottage', 'Beach']
        for p in products:
            p.category = random.choice(categories)
            p.status = 'active' if random.random() > 0.1 else 'inactive'
            p.save()

        # 2. Add some User-like data (if not enough)
        if User.objects.count() < 10:
            for i in range(10):
                User.objects.create_user(
                    username=f'user_{i+1}', 
                    email=f'user_{i+1}@example.com',
                    password='password123'
                )

        users = User.objects.all()

        # 3. Add sample Bookings
        today = date.today()
        status_options = ['confirmed', 'pending', 'cancelled']
        for _ in range(30):
            p = random.choice(products)
            u = random.choice(users)
            Booking.objects.create(
                product=p,
                user=u,
                user_name=u.username,
                date=today - timedelta(days=random.randint(1, 10)),
                price=p.price,
                status=random.choice(status_options)
            )

        # 4. Add sample Reviews
        for _ in range(20):
            p = random.choice(products)
            u = random.choice(users)
            Review.objects.create(
                product=p,
                user=u,
                user_name=u.username,
                rating=random.randint(3, 5),
                comment="Great place, loved it!"
            )

        # 5. Add sample Activities
        activities = [
            ("New user registered", "alexander.taylor@email.com", "user"),
            ("New booking received", "Chimgan Mountain Cottage", "shopping"),
            ("New review posted", "5-star review for Amirsoy Villa", "message"),
            ("Payment received", "$250 from John Doe", "dollar"),
            ("Booking confirmed", "Charvak Lake House", "calendar"),
        ]
        for title, desc, icon in activities:
            Activity.objects.create(
                title=title,
                description=desc,
                icon_type=icon
            )

        # 6. Add sample Employees
        employees = [
            ("John Smith", "Manager", "john@dachago.uz", "+998 90 123-45-67"),
            ("Sarah Johnson", "Front Desk", "sarah@dachago.uz", "+998 90 234-56-78"),
            ("Mike Chen", "Maintenance", "mike@dachago.uz", "+998 90 345-67-89"),
            ("Elena Petrova", "Cleaning", "elena@dachago.uz", "+998 90 456-78-90"),
        ]
        for name, pos, email, phone in employees:
            Employee.objects.create(name=name, position=pos, email=email, phone=phone)

        # 7. Add sample Payments
        methods = ["Credit Card", "PayPal", "Bank Transfer"]
        for i in range(10):
            Payment.objects.create(
                transaction_id=f"PAY{100+i}",
                customer_name=f"Customer {i+1}",
                cottage_name=random.choice(products).title,
                amount=random.randint(100, 500),
                method=random.choice(methods),
                status=random.choice(['completed', 'pending', 'failed']),
                date=today - timedelta(days=random.randint(0, 5))
            )

        # 8. Add sample Services
        services = [
            ("BBQ Equipment", 25, "Per Event"),
            ("Swimming Pool", 50, "Per Day"),
            ("Sauna", 35, "Per Hour"),
            ("Karaoke", 40, "Per Event"),
        ]
        for name, price, duration in services:
            Service.objects.create(name=name, price=price, duration=duration)

        # 9. Add sample Announcements
        announcements = [
            ("New Year Discount 50%", "Get 50% off on all bookings this New Year!", today - timedelta(days=5)),
            ("Seasonal Promotion", "Summer special - Book 3 days get 1 free!", today - timedelta(days=10)),
            ("Maintenance Notice", "Chimgan Cottage will be under maintenance from Feb 20-22", today),
        ]
        for title, content, date_val in announcements:
            Announcement.objects.create(title=title, content=content, date=date_val, views=random.randint(100, 2000))

        # 10. Default Settings
        Settings.objects.get_or_create(id=1)

        self.stdout.write(self.style.SUCCESS('Successfully populated all dashboard data'))
