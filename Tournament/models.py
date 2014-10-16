from django.db import models


#These constants map the events to a two letter abbreviation

ORIGINAL_ORATORY = 'OO'
STANDARD_ORATORY = 'SO'
PROSE = 'PR'
DRAMATIC_INTERP = 'DI'
HUMOROUS_INTERP = 'HI'
FOREIGN_EXTEMP = 'FX'
DOMESTIC_EXTEMP = 'DX'
MONOLOGUE = 'MO'
LD_DEBATE = 'LD'
POETRY = 'PO'
CROSS_EXAM_DEBATE = 'CX'
HUMOROUS_DUET = 'HD'
DRAMATIC_DUET = 'DD'
PUBLIC_FORUM = 'PF'

EVENT_CHOICES = (
    (ORIGINAL_ORATORY, 'OO'),
    (STANDARD_ORATORY, 'SO'),
    (PROSE, 'PR'),
    (DRAMATIC_INTERP, 'DI'),
    (HUMOROUS_INTERP, 'HI'),
    (FOREIGN_EXTEMP, 'FX'),
    (DOMESTIC_EXTEMP, 'DI'),
    (MONOLOGUE, 'MO'),
    (LD_DEBATE, 'LD'),
    (POETRY, 'PO'),
    (CROSS_EXAM_DEBATE, 'CX'),
    (HUMOROUS_DUET, 'HD'),
    (DRAMATIC_DUET, 'DD'),
    (PUBLIC_FORUM, 'PF') )


# Create your models here.

class Person(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    events = models.CharField(max_length=2, choices=EVENT_CHOICES)


class School(models.Model):
    """
    Model representation of a school. Maps a one-to-many relationship with
    students, coaches, and judges.
    """
    registration_date = models.DateTimeField()


class Student(models.Model):
    """
    Model representation of a student/competitor in the tournament.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    school = models.ForeignKey(School)
    registration_date = models.DateTimeField()

    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES, default=FRESHMAN)

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)

class Coach(models.Model):
    """
    Model representation of a coach.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    school = models.ForeignKey(School)
    registration_date = models.DateTimeField()

class Building(models.Model):
    """
    Representation of the tournament venue. Maintains a one-to-many relationship with
    room objects.
    """
    school = models.ForeignKey(School)
    rooms = models.ForeignKey(Room)


class Room(models.Model):
    """
    Representation of individual rooms at a tournament venue. Maintains a many-to-one relationship
    with Building objects.
    """
    school = models.OneToOneField(School)
    capacity = models.IntegerField()


class Judge(models.Model):
    """
    Model representation of a Judge.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)