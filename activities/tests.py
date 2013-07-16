from django.test import TestCase
from activities import custom_validators 
from activities.models import Activity
from datetime import date, timedelta
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

class CustomValidatorsTests(TestCase):
    
    def test_date_not_in_future(self):
        """
        Tests that the custom_validators.date_not_in_future function works as expected for current and past dates
        """

        # No exception should be thrown
        custom_validators.date_not_in_future(date.today())

        # No exception should be thrown
        custom_validators.date_not_in_future(date.today() - timedelta(days=1))

    def test_date_in_future(self):
        """
        Tests that the custom_validators.date_not_in_future throws an exception when the date is in the future
        """

        tomorrow = date.today() + timedelta(days=1)

        with self.assertRaises(ValidationError) as ctx:
            custom_validators.date_not_in_future(tomorrow)
 
class ActivitiesViewTests(TestCase):

    def test_display_none(self):
        """
        Tests that the activities listing correct displays no activities when they don't exist.
        """

        response = self.client.get(reverse("activities:index"))
        self.assertEqual(response.status_code, 200);
        self.assertContains(response, "No activities are available.")
        self.assertQuerysetEqual(response.context["recent_activities"], [])

    def test_display_one(self):
        """
        Tests that the activities listing correctly displays a single activity that was previously created.
        """

        create_activity(name="activity 1")
        response = self.client.get(reverse("activities:index"))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "No activities are available")
        self.assertQuerysetEqual(response.context["recent_activities"], 
            ['<Activity: activity 1>']
        )

    def test_display_two(self):
        """
        Tests that the activities listing correctly displays two activities that were previously created.
        """

        create_activity(name="activity 1")
        create_activity(name="activity 2")
        response = self.client.get(reverse("activities:index"))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "No activities are available")
        self.assertQuerysetEqual(response.context["recent_activities"],
            ['<Activity: activity 1>', '<Activity: activity 2>']
        )

def create_activity(name):
    """
    Factory method to create a mock activity with the name specified.
    """

    return Activity.objects.create(name=name, type="RUNNING", date=date.today(), desc="Generic description")
