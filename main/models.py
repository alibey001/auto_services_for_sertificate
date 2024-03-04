from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from .validators import ImageFileValidator
import qrcode
from io import BytesIO
from django.core.files import File




class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True, verbose_name='FIO')
    password = models.CharField(max_length=255, verbose_name='Parol', validators=[
        RegexValidator(
            regex='(?=^.{8}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.[A-Z])(?=.*[a-z]).*$',
            message='Invalid password number',
            code='password number'
        )
    ])
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name='Manzilingizni kriting')
    phone_number = models.CharField(max_length=13, unique=True,verbose_name='Telefon raqamingizni kiriting', validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number',
        )])
    age = models.IntegerField(verbose_name='Yoshi', null=True)
    email = models.CharField(max_length=255, verbose_name='Email', validators=[
        RegexValidator(
            regex='^[-\w.]+@([A-z0-9]+\.)+[A-z]{2,4}$',
            message = 'Invalide email',
            code = 'Invalid email'
        )
    ])
    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Foydalanuvchi'


    def clean(self):
        if self.age < 18:
            raise ValidationError("a citizen under the age of 18 will not be employed")



class Employee(models.Model):
    user = models.OneToOneField(to='User', on_delete=models.CASCADE,  verbose_name='Foydalanuvchi')
    profession = models.ForeignKey(to='Profession', verbose_name='Kasbi', on_delete=models.CASCADE)
    wages = models.CharField(max_length=255,  verbose_name='Ish haqi')
    age = models.IntegerField(default=18,  verbose_name='Yosh')
    address = models.CharField(max_length=255,  verbose_name='Manzil')
    experience = models.CharField(max_length=255,  verbose_name='Tajriba')
    start_work_time = models.TimeField(verbose_name='Ish boshlanish vaqti')
    end_work_time = models.TimeField(verbose_name='Ish tugashi vaqti')
    rating = models.CharField(max_length=255,  verbose_name='Reting')
    garaj = models.OneToOneField(to='Garaj', null=True, blank=True, verbose_name='Garaj', on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Ishchilar'

    def __str__(self):
        return f"{self.user.username}"


class Profession(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nomi')

    class Meta:
        verbose_name = 'Profession'
        verbose_name_plural = 'Kasbi'

    def __str__(self):
        return self.name


class Order(models.Model):
    employee = models.ForeignKey(to='Employee', on_delete=models.CASCADE, verbose_name='Ishchi')
    code = models.CharField(max_length=55, verbose_name='Buyurtma kodi')
    owner_name = models.CharField(max_length=255,  verbose_name='moshinani egasini ismi')
    owner_phone_number = models.CharField(max_length=13, verbose_name='Mijozning telefon raqami', validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    is_delivery = models.BooleanField(default=False, verbose_name='Band')
    address = models.CharField(max_length=255,  verbose_name='Manzil')
    car_name = models.CharField(max_length=55,  verbose_name='Moshina rusimi')
    car_number = models.CharField(max_length=8, verbose_name='Moshina raqami')
    is_acitve = models.BooleanField(default=1, verbose_name='Band', choices=(
        ( 1,'kutyapti' ),
        ( 2,'koryapti' ),
        ( 3,'korib boldi' ),
    ))
    problem = models.TextField(null=True, blank=True,  verbose_name='Muamosi')
    services_cost = models.CharField(max_length=255, verbose_name='Servis narxi', null=True, blank=True)
    start_day = models.DateField(auto_now=True, verbose_name='Boshlnish kuni')
    start_time = models.TimeField(auto_now=True,verbose_name='Boshlanish vaqti')
    end_date = models.DateField(null=True, blank=True, verbose_name='Tugash kuni')
    end_time = models.TimeField(null=True, blank=True, verbose_name='Tugash vaqti')
    qr_code = models.ImageField(upload_to='order_qr_codes/', blank=True, null=True)
    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=5,
            border=3,
        )
        qr.add_data(f"Yourto encode in the QR code: {self.code}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Buyurtma'

    def __str__(self):
        return self.owner_name


class Payment(models.Model):
    order = models.ForeignKey(to='Order', on_delete=models.CASCADE,  verbose_name='Buyurtma qilish')
    code = models.CharField(max_length=55, verbose_name='Kod')
    created_at = models.DateTimeField(auto_now=True)
    date = models.DateField(verbose_name='kun')
    payment_type = models.IntegerField(default=2, verbose_name='Tolash yoli', choices=(
        (1,'card'),
        (2,'cash'),
        (3,'other')
    ))
    admin = models.ForeignKey(to='Employee', on_delete=models.CASCADE,  verbose_name='admin')
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True, verbose_name='QR code')


    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=5,
            border=3,
        )
        qr.add_data(f"Your data to encode in the QR code:{self.code}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Tolov'

    def __str__(self):
        return self.code


class Comment(models.Model):
    order = models.ForeignKey(to='Order', verbose_name='Buyurtma qilish', on_delete=models.CASCADE)
    type = models.IntegerField(default=1, verbose_name='Izoh turi', choices=(
        (1, 'comment'),
        (2, 'complain'),
        (3, 'Offer'),
    ))
    create_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Izoh'

class Cassa(models.Model):
    total_summa = models.PositiveIntegerField(verbose_name='Hisob')


    class Meta:
        verbose_name = 'Cassa'
        verbose_name_plural = 'Kassa'


class Garaj(models.Model):
    name = models.CharField(max_length=255, unique=True,  verbose_name='Nomi')


    class Meta:
        verbose_name = 'Garaj'
        verbose_name_plural = 'Garaj'

    def __str__(self):
        return self.name


class Report(models.Model):
    income = models.PositiveIntegerField(verbose_name='Kirim')
    cost = models.PositiveIntegerField(verbose_name='Chiqim')
    work_done = models.TextField(verbose_name='Qilingan ish')
    order = models.ForeignKey(to='Order', verbose_name='Buyurtma', on_delete=models.CASCADE)
    employee = models.ForeignKey(to='Employee', verbose_name='Ishchi', on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Hisobot'

    def __str__(self):
        return self.income



class Attendence(models.Model):
    employee = models.ForeignKey(to='Employee', on_delete=models.CASCADE, verbose_name='ishchi')
    date = models.DateField(verbose_name='kun')
    check_in = models.TimeField(null=True, blank=True, verbose_name='Kirish')
    check_out = models.TimeField(null=True, blank=True, verbose_name='chiqish')


    class Meta:
        verbose_name = 'Attendence'
        verbose_name_plural = 'Davomat'
        unique_together = ['employee', 'date']


    def clean(self):
        if self.check_out and self.check_out < self.check_in:
            raise ValidationError("Check-out time must be after check-in time.")

    def __str__(self):
        return f"{self.employee} - {self.date}"