from django.test import TestCase
from datetime import datetime
from .models import Reservation
# Create your tests here.


class ReservationModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.reservation = Reservation.objects.create(
            name='John Doe',
            phone_number='1234567890',
            reservation_count=4,
            comments='Birthday celebration'
        )

    def test_fields(self):
        self.assertIsInstance(self.reservation.name, str)

        self.assertIsInstance(self.reservation.phone_number, str)

        self.assertIsInstance(self.reservation.reservation_count, int)

        self.assertIsInstance(self.reservation.comments, str)

    def test_timestamps(self):
        self.assertIsInstance(self.reservation.reservation_date, datetime)
