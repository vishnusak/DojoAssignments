# Task Manager - Ajax Assignment

### What works:
+ Front-end
  - Single Page to show Tasks and form for adding new tasks
    - Each task has a checkbox next to it for marking completion
    - Each task has an edit button next to it for modifying/updating the task
  - Partial for refreshing the displayed tasks

+ Back-end
  - ERD, Schema generation and Setup
  - Single table used
  - Used a column called "deleted" to mark completed tasks instead of deleting them.
    - This is done to ensure we can still display the "deleted" tasks grayed out on the UI

+ Controllers and Models
  - Tasks / Task (controller / model) for handling the CRUD

+ UX
  - Show list of existing tasks on loading the page
  - Use the form on the right to add new tasks
  - In the task list on the left
    - Click the "Edit" button against any task to enable editing the task.
      - On completion, click the "Save" button to save the updated task.
    - Click on the "checkbox" to mark a task as completed.
      - The checkbox, task and button get disabled
      - The button will now show "Done"
  - The task list on the left will show a scroll bar if the number of tasks becomes high.
