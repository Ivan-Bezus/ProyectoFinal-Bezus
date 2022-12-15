import datetime
from EmpApp1.models import Booking


def check_availability(date_in, date_out):
    avail_list=[]
    booking_list = Booking.objects.all()
    for booking in booking_list:
        if booking.date_in > date_out or booking.date_out < date_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)