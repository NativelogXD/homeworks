# Product Specification: Household Chores Manager (Family Edition)

## 1. Overview
A lightweight web application for families (parents and children) to manage and track recurring weekly household chores without friction or complex approval flows.

## 2. Core Users
- **Family Members:** Parents and children living in the same home.

## 3. Scope & Key Features (MVP)
1. **Family Members & Chore Catalog:**
   - Define family members (name, role/tag).
   - Create recurring household chores assigned to a specific member and a fixed day of the week (Monday through Sunday).
2. **Weekly Family Dashboard:**
   - A weekly grid overview displaying all scheduled tasks for each day and family member.
3. **Personal Daily View ("My Day"):**
   - Filter by family member to view only today's pending chores.
   - Quick toggle checkbox to mark chores as "Pending" or "Completed".

## 4. Out of Scope (Future Versions)
- Complex point/reward economy or coin redemption.
- Manual parent approval workflows for completed tasks.
- Mobile push notifications.

## 5. Non-Functional Constraints
- Built with Python & Django.
- SQLite for local storage (zero configuration).
- Simple, responsive web interface using standard HTML/CSS.
- Independent automated tests for model and views.
