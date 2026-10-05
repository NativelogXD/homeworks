# Backlog: Household Chores Manager

## 1. Setup Django project with initial chore models and test
Goal: Configure the Django app and define the database models for FamilyMember and Chore with an initial passing test.
Description: Initialize Django and create the `chores` app registered in `config/settings.py`. Implement the `FamilyMember` and `Chore` models in `chores/models.py`, generate database migrations, and write an initial test in `chores/tests.py` verifying model creation.

## 2. Implement the Weekly Family Dashboard view
Goal: Render a weekly grid view showing scheduled chores across all days and members.
Description: Create a view in `chores/views.py` and a template displaying chores grouped by day of the week (Monday through Sunday) and family member. Wire the route in `config/urls.py` and add a test verifying HTTP 200 response.

## 3. Implement Personal Daily View ("My Day")
Goal: Provide a filtered view for a selected family member showing only today's chores.
Description: Add a view that accepts a family member selection and filters chores for the current day of the week. Include a test verifying filtered results.

## 4. Add interactive completion toggle
Goal: Allow users to toggle chore status between Pending and Completed.
Description: Create an action view to toggle `is_completed` for a chore and update the interface. Add tests verifying status change in the database.
