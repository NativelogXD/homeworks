from django.test import TestCase
from chores.models import FamilyMember, Chore


class FamilyMemberModelTest(TestCase):
    def test_create_family_member(self):
        member = FamilyMember.objects.create(name="Alice", role="Parent")
        self.assertEqual(member.name, "Alice")
        self.assertEqual(member.role, "Parent")
        self.assertEqual(str(member), "Alice")

    def test_default_role(self):
        member = FamilyMember.objects.create(name="Bob")
        self.assertEqual(member.role, "Member")


class ChoreModelTest(TestCase):
    def setUp(self):
        self.member = FamilyMember.objects.create(name="Charlie", role="Child")

    def test_create_chore(self):
        chore = Chore.objects.create(
            title="Clean bedroom",
            assigned_to=self.member,
            day_of_week="saturday",
            is_completed=False,
        )
        self.assertEqual(chore.title, "Clean bedroom")
        self.assertEqual(chore.assigned_to, self.member)
        self.assertEqual(chore.day_of_week, "saturday")
        self.assertFalse(chore.is_completed)
        self.assertEqual(str(chore), "Clean bedroom (Charlie)")

    def test_chore_default_values(self):
        chore = Chore.objects.create(
            title="Wash dishes",
            assigned_to=self.member,
        )
        self.assertEqual(chore.day_of_week, "monday")
        self.assertFalse(chore.is_completed)

    def test_member_chores_relationship(self):
        Chore.objects.create(title="Water plants", assigned_to=self.member)
        Chore.objects.create(title="Walk dog", assigned_to=self.member)
        self.assertEqual(self.member.chores.count(), 2)
