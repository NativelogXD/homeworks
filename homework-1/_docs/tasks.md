# Tasks Backlog

## 1. Setup project and base models with a passing test
Goal: Initialize the Django application with core models and verify setup with automated tests.
Description: Configure the Django project using uv and create the `chores` app. Define the initial data models for `FamilyMember` and `Chore` according to the plan specification. Add an initial unit test to verify that models can be created and that the test suite passes.

## 2. Weekly Family Dashboard
Goal: Provide a weekly grid overview displaying all chores scheduled by day and family member.
Description: Implement a dashboard view and template showing a Monday-to-Sunday matrix. Each cell should display chores assigned to family members for that specific day of the week.

## 3. Personal Daily View ("My Day")
Goal: Allow family members to view their specific chores scheduled for the current day.
Description: Create a personalized view that filters chores by the selected family member and today's day of the week. Display chore details with clear indicators of pending or completed status.

## 4. Quick Toggle Chore Status
Goal: Enable immediate status toggling of chores between Pending and Completed.
Description: Implement an endpoint and interactive UI mechanism to toggle chore completion status without full page reload friction. Ensure state persistence in the database and clear visual feedback.
