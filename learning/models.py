import pytz

from typing import Final, final

from datetime import datetime

from django.db import models

# Create your models here.

_FIELDS_MAX_LENGTH: Final = 50

@final
class Student(models.Model):
    """
    Represents a student in the database. 
    """

    first_name = models.CharField(max_length=_FIELDS_MAX_LENGTH)
    last_name = models.CharField(max_length=_FIELDS_MAX_LENGTH)
    patronymic = models.CharField(max_length=_FIELDS_MAX_LENGTH)
    birthday = models.DateField(default=datetime.now(tz=pytz.UTC))
    email = models.CharField(max_length=_FIELDS_MAX_LENGTH)
    followed_courses = models.ManyToManyField('Course')

    class Meta(object):
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self) -> str:
        """All django models should have this method."""
        return '<Student: {0} {1} {2}, email: {3}>'.format(
            self.last_name,
            self.first_name,
            self.patronymic,
            self.email
        )


@final
class Course(models.Model):
    """
    Represents a course in the database.
    """

    name = models.CharField(max_length=_FIELDS_MAX_LENGTH)
    start_time = models.DateField(default=datetime.now(tz=pytz.UTC))
    end_time = models.DateField(default=datetime.now(tz=pytz.UTC))

    class Meta(object):
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self) -> str:
        """All django models should have this method."""
        return '<Course: {0}, start time: {1}, end time: {2}>'.format(
            self.name,
            self.start_time,
            self.end_time
            )


@final
class Lecture(models.Model):
    """
    Represents a lecture in the database.
    """

    name = models.CharField(max_length=_FIELDS_MAX_LENGTH)
    date = models.DateField(default=datetime.now(tz=pytz.UTC))
    related_course = models.ForeignKey(
        'Course',
        null=True,
        default=None,
        on_delete=models.SET_NULL,
    )

    class Meta(object):
        verbose_name = 'Lecture'
        verbose_name_plural = 'Lectures'

    def __str__(self) -> str:
        """All django models should have this method."""
        return '<Lecture: {0}, date: {1}>'.format(self.name, self.date)