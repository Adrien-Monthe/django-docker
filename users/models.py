
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# Create your models here.


# *---*---*---*---*---*---*  S O F T D E L E T E M O D E L  B E G I N  *---*---*---*---*---*---*

class TimeStampModel(models.Model):
    deleted_at = models.DateTimeField(null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True


# *---*---*---*---*---*---*  S O F T D E L E T E M O D E L  E N D  *---*---*---*---*---*---*


# *---*---*---*---*---*---* L A N G U A G E   B E G I N            *---*---*---*---*---*---*

class Language(TimeStampModel):
    name = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        db_table = 'languages'
        ordering = ['name']

    def __str__(self):
        return self.name


# *---*---*---*---*---*---*  L A N G U A G E   E N D    *---*---*---*---*---*---*


# *---*---*---*---*---*---* A D D R E S S     B E G I N *---*---*---*---*---*---*

class Address(TimeStampModel):
    postal_code = models.CharField(blank=True, null=True, max_length=255)
    street = models.CharField(blank=True, null=True, max_length=255)
    city = models.CharField(blank=True, null=True, max_length=255)
    state = models.CharField(blank=True, null=True, max_length=255)
    country = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        db_table = 'addresses'

    # def __str__(self):
    # return self.id


# *---*---*---*---*---*---*  A D D R E S S  E N D  *---*---*---*---*---*---*


# *---*---*---*---*---*---* I M A G E  B E G I N   *---*---*---*---*---*---*

class Image(TimeStampModel):
    filename = models.CharField(blank=True, null=True, max_length=255)
    url = models.ImageField(blank=True)

    class Meta:
        db_table = 'images'
        ordering = ['filename']

    def __str__(self):
        return self.filename


# *---*---*---*---*---*---*  I M A G E   E N D           *---*---*---*---*---*---*


# *---*---*---*---*---*---* S P E C I A L T Y  B E G I N *---*---*---*---*---*---*

class Speciality(TimeStampModel):
    SPECIALITIES = [
        (0, 'Médecin généraliste'),
        (1, 'Médecin de famille'),
        (2, 'Pédiatre'),
        (3, 'Psychologue'),
        (4, 'Chirurgien'),
        (5, 'Interniste'),
        (6, 'Gynéco-obstétrique'),
        (7, 'Urologiste'),
        (8, 'Médecine traditionnelle'),
    ]
    label = models.IntegerField(blank=True, null=True, choices=SPECIALITIES, max_length=255)



    def __str__(self):
        return self.label


# *---*---*---*---*---*---*  S P E C I A L T Y   E N D  *---*---*---*---*---*---*


class User(AbstractUser):
    GENDER = [
        ('M', 'Homme'),
        ('F', 'Femme'),
        ('O', 'Autre'),
    ]
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(blank=True)
    gender = models.CharField(null=True, blank=True, choices=GENDER, max_length=254)
    birth_date = models.DateField(null=True, blank=True, )
    phone_number = models.CharField(null=True, blank=True, max_length=254)
    deleted_at = models.DateTimeField(null=True, default=None)

    def __str__(self):
        return self.username


# *---*---*---*---*---*---* P A T I E N T  B E G I N *---*---*---*---*---*---*

class Patient(TimeStampModel):
    MARITAL_STATUS = [
        (0, 'Célibataire'),
        (1, 'Conjoint de fait'),
        (2, 'Mariée'),
        (3, 'Veuf(ve)'),
        (4, 'Divorcé(e)'),
        (5, 'Autre'),
    ]
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    marital_status = models.IntegerField(blank=True, choices=MARITAL_STATUS, null=True, max_length=255)
    job_title = models.CharField(blank=True, null=True, max_length=255)

    def __str__(self):
        return "%s The Patient" % self.user.first_name

# *---*---*---*---*---*---*  P A T I E N T   E N D             *---*---*---*---*---*---*


# *---*---*---*---*---*---* P R O F E S S I O N A L  B E G I N *---*---*---*---*---*---*

class Professional(TimeStampModel):
    STATUS_NAMES = [
        (0, 'Approbation en cours'),
        (1, 'Dossier approuvé'),
        (2, 'Dossier refusé'),

    ]
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    is_professional_order = models.CharField(blank=True, null=True, max_length=255)
    job_title = models.CharField(blank=True, null=True, max_length=255)
    activation_date = models.DateTimeField(null=True, default=None)

    def __str__(self):
        return "%s The Patient" % self.user.first_name

# *---*---*---*---*---*---*  P R O F E S S I O N A L   E N D  *---*---*---*---*---*---*
