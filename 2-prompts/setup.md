# Setup Prompt

This prompt should be run before generating any CV or cover letter. It ensures the user's profile data is ready.

## Step 1: Check Profile Data

Read the `0-profile/` folder and check if the user has added at least one CV data file (e.g., a file containing work experience, education, skills, etc.).

- If `0-profile/` only contains `user-preferences.md` and `additional-skill-information.md` (both empty or default), remind the user:
  > "You haven't added your CV data yet. Please add at least one file with your CV information (work experience, education, skills, etc.) to the `0-profile/` folder before proceeding."
- If the user has PDF files in `0-profile/`, convert them to Markdown automatically by running:
  ```
  pip install pymupdf
  python scripts/pdf-to-md.py
  ```
  After conversion is done, confirm to the user which files were converted and proceed to Step 2.
- If CV data `.md` files exist, proceed to Step 2.

## Step 2: Collect User Preferences

Read the template at `3-templates/user-preferences-template.md` to understand what information needs to be collected.

Then check `0-profile/user-preferences.md`:
- If preferences are already filled in, confirm with the user if they want to update anything.
- If preferences are empty or incomplete, present all questions at once so the user can answer them in a single response:

  > Please provide the following preferences (you can answer all at once):
  >
  > 1. **Work Preference** — Office / Hybrid / Remote / Open to Any
  > 2. **CV & Cover Letter Language** — English / Bahasa Indonesia / Other
  > 3. **Expected Annual Salary** — e.g., Minimum $30,000 / Negotiable / Prefer not to disclose
  > 4. **Earliest Start Date** — e.g., Immediately / September 2026 / 1 month notice
  > 5. **Additional Notes** — anything else you want the AI to consider (optional)

After the user responds, save/update all answers to `0-profile/user-preferences.md` at once.

If the user selected **Remote** or **Hybrid** as their work preference, follow up with:
  > You mentioned you prefer remote/hybrid work. Do you have prior remote working experience? If yes, how long have you been working remotely?

Save the answer to `0-profile/user-preferences.md` under "Remote Experience". If the user has remote experience, highlight it in the CV summary when generating.

## Step 3: Confirmation

Once both profile data and preferences are ready, ask the user:
> "Your profile is set up and ready. Do you want to proceed with generating your CV and cover letter now?"

If the user confirms yes, immediately proceed to run the prompt in `generate-cv-cover-letter.md`.
