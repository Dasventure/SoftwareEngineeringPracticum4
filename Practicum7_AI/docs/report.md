## Report

### What was the prompt you used?

The prompt I used for GitHub Copilot can be found in `prompts/P1.txt`. In the prompt the following is stated or provided:

(1) The role the AI agent should take on ("senior software engineer").

(2) The context files, further explained below.

(3) The non-functional requirements; explicitly manually written down from session 2. I have chosen to take the AI generated NF's here.
The manual team will then use the manually made NF's from session 2.

(4) The actual task: review, select 4 issues, write comments

(5) The format of a comment: location (file + lines), issue, why it matters now (NF's), suggestion, tone 

(6) Some extra rules, further explained below.

### What else did you feed to the AI coding agent?

I added extra context files: `docs/requirements.md` and `docs/review-guidelines.md`. These reflect the requirements and guidelines from the assignment document. Additionally, the folder `pull_request_code` was provided, this is the exact folder as attachment from the assignment zip.

As for the extra rules, I asked to only use the provided context and specified a review comment should be max 150 words. This prevents the AI from generating too much information and ensures a concise review.

I also added a "tone", specifying the goal is: "constructive motivating the submitter of the pull request to address and resubmit".

### What did you do to efficiently feed context to the AI coding agent?

All context expect for the code itself are short checklists. Often times defined in md files, for the NF's I went a step further and directly stated them inside the prompt. I efficiently ordered the NF's in a short bullet list, each entry: 

`NF-<number>: <quality attribute>: <one-liner sentence link to the system>`

The reader of the review is assumed to have the list of non-functional requirements with the correct number references. (from session 2)

Some NF's in that list are irrelevant to this specific pull request that the AI agent reviews. However, I still chose to add them for following reason: the prompt I made can essentially now be reused as template for any incoming pull request about the same university platform system.

### Which issues did the AI coding agent choose?

They chose: "Facility types are still hardcoded", "Facility access is not restricted to administrators", "Facility retrieval and modification are incomplete" and "User registration contains broken control flow".

### Which reviews did the AI coding agent create?

The full review document can be found in `output/pull_request_review.md`. It contains the four issues with comments (aka the review) under them in the specified format (location - issue - why it matters now - suggestion)

Quick mention: The AI hallucinated heavily at issue 4. It added integer raises to the issue and even provided a typed exception as suggestion. However, the review-guidelines document explicitly mentions to ignore integer exceptions!