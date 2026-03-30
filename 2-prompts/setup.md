# Setup Prompt

This prompt should be run before generating any CV or cover letter. It ensures the user's profile data is ready.

## Step 1: Check Profile Data

Read the `0-profile/` folder and check if the user has added at least one CV data file (e.g., a file containing work experience, education, skills, etc.).

- If `0-profile/` only contains `user-preferences.md` and `additional-skill-information.md` (both empty or default), remind the user:
  > "You haven't added your CV data yet. Please add at least one file with your CV information (work experience, education, skills, etc.) to the `0-profile/` folder before proceeding."
- If CV data files exist, proceed to Step 2.

## Step 2: Collect User Preferences

Read the template at `3-templates/user-preferences-template.md` to understand what information needs to be collected.

Then check `0-profile/user-preferences.md`:
- If preferences are already filled in, confirm with the user if they want to update anything.
- If preferences are empty or incomplete, ask the user to provide the following information one by one:
  1. Work Preference (Office / Hybrid / Remote / Open to Any)
  2. CV & Cover Letter Language (English / Bahasa Indonesia / Other)
  3. Expected Annual Salary (or "Prefer not to disclose")
  4. Earliest Start Date
  5. Any additional notes

After the user provides each answer, save/update the responses to `0-profile/user-preferences.md`.

## Step 3: Confirmation

Once both profile data and preferences are ready, confirm to the user:
> "Your profile is set up and ready. You can now proceed with generating your CV and cover letter using the main prompt."
