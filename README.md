# AI CV & Cover Letter Generator

An AI-powered project that generates tailored CVs and cover letters based on your profile data and job descriptions. Designed to work with any AI assistant or IDE that can read and write files, such as:

- [Kiro](https://kiro.dev)
- [Cursor](https://cursor.sh)
- [GitHub Copilot Chat](https://github.com/features/copilot)
- [Gemini CLI](https://geminicli.com)
- Or any AI assistant with file access capabilities

## Why This Project Exists

1. Most companies now use AI-based screening in their early hiring stages. If your CV isn't well-aligned with the job requirements, it may get filtered out before a human ever sees it.

2. As someone who also reviews candidates, I often see CVs that are clearly mass-sent across dozens of job postings. They're too generic — making it hard to tell whether the candidate actually meets specific requirements, simply because the relevant skills aren't highlighted or mentioned.

3. Creating a tailored CV for every application is time-consuming. This project solves that by generating CVs that are dynamic and flexible — adapting to both your actual skills and the specific job requirements — so each application is more effective and on target.

## How It Works

1. Add your CV/profile data to `0-profile/`
2. Paste a job description into `1-jobs/jobdesk.md`
3. Run the setup prompt to configure your preferences
4. Run the generate prompt — the AI creates a tailored CV and cover letter

![img_23.png](examples/img_23.png)

## Project Structure

```
0-profile/          → Your personal data (CV, skills, preferences)
1-jobs/             → Job description to apply for
2-prompts/          → AI prompts that drive the generation
3-templates/        → Templates for CV, cover letter, and preferences
4-output/           → Generated results (CV + cover letter in .md and .html)
examples/           → Screenshots and videos for documentation
scripts/            → Utility scripts (e.g., PDF to Markdown converter)
```

## Getting Started

### 0. Clone the Repository

```bash
git clone https://github.com/ifanzalukhu97/AI-CV-Cover-Letter-Generator.git
cd AI-CV-Cover-Letter-Generator
```

### 1. Add Your Profile Data

Place your CV or resume files in the `0-profile/` folder. You can get your CV data from various sources:

- **LinkedIn** — export or copy your LinkedIn profile. [How to export your profile as PDF](https://www.linkedin.com/help/linkedin/answer/a8313636)
- **Glints, JobStreet, or other job platforms** — download or copy your profile/CV. [How to generate CV from Glints](https://help.glints.com/hc/en-us/articles/49175868569369-Generate-Your-CV-from-Your-Profile-on-the-Glints-App)
- **Your latest CV** — any existing CV document you have

Supported formats:

- `.md` (Markdown) — ready to use
- `.pdf` — will be automatically converted to Markdown by the AI when you run the setup prompt

You can add multiple files from different sources — the AI will read all `.md` files in the folder and combine the information.

You can also manually convert PDFs if you prefer:

```bash
pip install pymupdf
python scripts/pdf-to-md.py
```


![image.png](examples/image.png)
In the image above, I'm using PDF format files. The AI will automatically convert them to Markdown when running the setup prompt. The converted files will be saved as `.md` in the same folder.

### 2. Add a Job Description

Paste the job description you want to apply for into `1-jobs/jobdesk.md`.

![img.png](examples/img.png)
Here I'm using a job description from LinkedIn for a Staff Software Engineer - .NET / API role.

### 3. Run Setup

Open `2-prompts/setup.md` and run it with your AI assistant. It will:
- Check if your profile data is ready (and auto-convert PDFs to Markdown if needed)
- Ask for your preferences (work arrangement, language, salary, start date)
- Save everything to `0-profile/user-preferences.md`
- Ask if you want to proceed to generate your CV and cover letter

![img_1.png](examples/img_1.png)
Here I started a chat with the prompt `Please run the prompt from the setup.md file`. You can use other languages too, for example Indonesian: `Tolong jalankan prompt di file setup.md`. Regardless of the language you communicate in, the CV output will follow your language preference settings.

![img_2.png](examples/img_2.png)
The AI starts understanding the context and workspace.

![img_3.png](examples/img_3.png)
Since my CV files are in PDF format, the AI will install the Python library and run the converter script.

![img_4.png](examples/img_4.png)
After installing the library, it runs the script. The profile folder now contains the converted `.md` files.

![img_5.png](examples/img_5.png)
Before proceeding, the AI will ask for your preferences — such as preferred language, work type (remote/hybrid/onsite), expected salary, and earliest start date. It will then save your preferences to `user-preferences.md`.

Simply fill in and answer the questions.
![img_6.png](examples/img_6.png)


### 4. Generate CV & Cover Letter

Run `2-prompts/generate-cv-cover-letter.md` with your AI assistant (or continue from setup). It will:
- Read your profile and the job description
- Identify gaps and ask for your input before proceeding
- Generate a tailored CV and cover letter
- Output results in both Markdown and HTML (A4 PDF-ready) to `4-output/`

After the setup prompt completes, it will offer to continue by running the `generate-cv-cover-letter.md` prompt. You can simply answer "yes".
This is an ongoing process.
![img_7.png](examples/img_7.png)

Here's an example when there are gaps in your profile.
The AI will ask and confirm first. It will then save the information to `additional-skill-information.md` for reference when generating the CV and cover letter, as well as for future runs.
![img_8.png](examples/img_8.png)

Just answer and explain:
![img_9.png](examples/img_9.png)

The AI automatically updates the `additional-skill-information.md` file with the additional information you provided. So next time you generate a CV and cover letter for a different job, the AI already has this extra data.
![img_10.png](examples/img_10.png)

And here are the generated CV and cover letter. You can open the Markdown files to see the content, or open the HTML files to view the PDF-formatted version.
![img_11.png](examples/img_11.png)
![img_12.png](examples/img_12.png)

## Prompts Overview

| File | Purpose |
|---|---|
| `setup.md` | Initial setup — checks profile, converts PDFs, collects preferences |
| `generate-cv-cover-letter.md` | Main prompt — generates tailored CV and cover letter |
| `convert-to-pdf.md` | Instructions for HTML/PDF output formatting |
| `persona.md` | AI persona — defines writing style and behavior |

## Out of Scope

This project focuses on CV and cover letter generation. The following are **not** included:
- Job searching or scraping

## Requirements

- An AI assistant that can read/write files (Kiro, Cursor, etc.)
- Python 3.x (only needed if you manually convert PDFs)

## Contributing

Contributions are welcome! If you have ideas for improvements, new templates, or better prompts:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'feat: add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Feel free to open an issue if you find bugs or have suggestions.

## Example Using Another AI Assistant (Gemini CLI)

Additional note:
The walkthrough above uses Kiro IDE, but you don't have to use Kiro. You can use any AI assistant that has file system access — such as Cursor, GitHub Copilot Chat, Gemini CLI, or any other AI assistant with similar capabilities.

Here's an example using Gemini CLI:
![img_14.png](examples/img_14.png)

Running the PDF to Markdown converter script:
![img_13.png](examples/img_13.png)

Collecting preferences and updating `user-preferences.md` with the provided information:
![img_15.png](examples/img_15.png)

![img_16.png](examples/img_16.png)

After the preference Q&A, it starts generating the CV and cover letter:
![img_17.png](examples/img_17.png)

Confirming profile gaps:
![img_18.png](examples/img_18.png)
![img_19.png](examples/img_19.png)

Done generating the CV and cover letter:
![img_20.png](examples/img_20.png)
![img_21.png](examples/img_21.png)
![img_22.png](examples/img_22.png)

## License

MIT
