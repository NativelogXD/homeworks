from django.db import models


class FamilyMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, default="Member")

    def __str__(self):
        return self.name


class Chore(models.Model):
    DAYS_OF_WEEK = [
        ("monday", "Monday"),
        ("tuesday", "Tuesday"),
        ("wednesday", "Wednesday"),
        ("thursday", "Thursday"),
        ("friday", "Friday"),
        ("saturday", "Saturday"),
        ("sunday", "Sunday"),
    ]

    title = models.CharField(max_length=200)
    assigned_to = models.ForeignKey(
        FamilyMember,
        on_delete=models.CASCADE,
        related_name="chores"
    )
    day_of_week = models.CharField(
        max_length=10,
        choices=DAYS_OF_WEEK,
        default="monday"
    )
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.assigned_to.name})"
