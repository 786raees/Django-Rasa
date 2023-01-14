from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _


class AllUser(AbstractUser):

    class UserType(models.TextChoices):
        student = 'student', 'student'
        teacher = 'teacher', 'teacher'
        doctor = 'doctor', 'doctor'

    class GENDER(models.TextChoices):
        male = 'male', 'male'
        female = 'female', 'female'

    user_type = models.CharField(max_length=11, choices=UserType.choices, default=UserType.doctor)
    gender = models.CharField(max_length=6, choices=GENDER.choices, default=GENDER.male)
    phone = models.CharField(_('phone'), max_length=150, null=True, blank=True)
    emergency_contact_number = models.CharField(_('Emergency Contact'), max_length=150, null=True, blank=True)
    photo = models.ImageField(_("user dp"), upload_to='user_photo',default='user_default_pic.jpg')
    current_address = models.TextField(_("current address"), null=True, blank=True)
    permanent_address = models.TextField(_("permanent address"), null=True, blank=True)
    id_number = models.CharField(_("ID Number"), max_length=10, null=True, blank=True)
    note = models.TextField(_("note"), null=True, blank=True)

    class Meta:
        verbose_name = _('All User')
        verbose_name_plural = _('All Users')

class StudentManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=AllUser.UserType.student)


class Student(AllUser):
    objects = StudentManager()

    class Meta:
        proxy = True
        verbose_name = _("student")
        verbose_name_plural = _("students")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = AllUser.UserType.student
        return super().save(*args, **kwargs)



class TeacherManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=AllUser.UserType.teacher)


class Teacher(AllUser):
    objects = TeacherManager()

    class Meta:
        proxy = True
        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = AllUser.UserType.teacher
        return super().save(*args, **kwargs)




class DoctorManager(UserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=AllUser.UserType.doctor)


class Doctor(AllUser):
    objects = DoctorManager()

    class Meta:
        proxy = True
        verbose_name = _("Doctor")
        verbose_name_plural = _("Doctors")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = AllUser.UserType.doctor
        return super().save(*args, **kwargs)


