# Prompt for Claude Code (paste this, and attach / point it to ANDROIDHASSAN-profile.zip)

You are working on my GitHub profile README. My GitHub username is **ANDROIDHASSAN**. The profile repo is **ANDROIDHASSAN/ANDROIDHASSAN** (default branch `main`). The zip `ANDROIDHASSAN-profile.zip` contains the finished files. Your job is to publish them exactly, make every image load, and turn on the automations. Do not redesign or rewrite any text.

## 1. Put the files in the repo
1. `gh repo clone ANDROIDHASSAN/ANDROIDHASSAN` (or use my existing local clone) and `git pull`.
2. Unzip `ANDROIDHASSAN-profile.zip` into the repo root, overwriting `README.md`. After unzipping the repo must contain:
   - `README.md`
   - `assets/` (18 SVG files: architecture, card-*, latency, neofetch, pipeline, voice-orb — each with `-dark.svg` and `-light.svg`)
   - `scripts/update_readme.py`
   - `.github/workflows/update-readme.yml` and `.github/workflows/snake.yml`
   - `REPO_README_TEMPLATE.md` and this `CLAUDE_CODE_PROMPT.md` (move both into a `docs/` folder so they don't clutter the root)
3. Delete the old stray file named `Hi, I'm @ANDROIDHASSAN` (note the spaces and apostrophe; quote the path).
4. Check that every `./assets/...svg` path referenced in `README.md` exists with exactly that name and case. Fix only paths, never text.
5. Commit with message `feat: voice-AI profile README with custom animated cards` and push to `main`.

## 2. Turn on the two workflows
1. Give Actions write access (needed to push the snake and the auto-updated list):
   `gh api -X PUT repos/ANDROIDHASSAN/ANDROIDHASSAN/actions/permissions/workflow -f default_workflow_permissions=write`
2. Run both workflows once:
   `gh workflow run snake.yml -R ANDROIDHASSAN/ANDROIDHASSAN`
   `gh workflow run update-readme.yml -R ANDROIDHASSAN/ANDROIDHASSAN`
3. Watch them with `gh run list -R ANDROIDHASSAN/ANDROIDHASSAN` and `gh run watch`. If one fails, read the log, fix the cause, and run it again. Then `git pull` so my local copy has the bot's commit.
4. Confirm the branch `output` now exists and contains `github-snake.svg` and `github-snake-dark.svg`.

## 3. Verify every image actually loads
For each of these, check that the URL returns HTTP 200 (use `curl -sI`):
- `https://raw.githubusercontent.com/ANDROIDHASSAN/ANDROIDHASSAN/main/assets/<file>` for all 18 SVGs
- `https://raw.githubusercontent.com/ANDROIDHASSAN/ANDROIDHASSAN/output/github-snake.svg` and `github-snake-dark.svg`
- every external image URL in `README.md` (capsule-render, readme-typing-svg, img.shields.io, skillicons.dev, streak-stats.demolab.com, the Animated-Fluent-Emojis raw links, the user-images GIFs)

Report any URL that is not 200 and fix it if the cause is on our side.

## 4. Update my profile fields
If `gh` lacks the `user` scope, run `gh auth refresh -h github.com -s user` and let me approve it. Then:
```bash
gh api -X PATCH user \
  -f name="Hassan Kazi" \
  -f bio="Voice AI engineer. Real-time voice agents in production (LiveKit). Rebuilding Indic STT/TTS from the papers up." \
  -f company="InCruiter" \
  -f location="Bengaluru, India" \
  -f blog="https://hassankazi3d.netlify.app"
```
This also removes the old `lockedin-verify-...` line from my bio.

## 5. Things you must NOT do without asking me first
- Do not archive, delete, rename or change the visibility of any of my other repos. Instead, give me a short list of repos you suggest archiving or making private (old tutorials, college work, forks I never changed) with one reason each, and wait for my OK.
- Do not touch any repo other than ANDROIDHASSAN/ANDROIDHASSAN.
- Do not edit README text, numbers or project statuses. They are deliberately honest (prod / building / next / planned / in review).
- Do not commit any token, key or `.env` file.

## 6. When you are done, tell me
- the commit link,
- whether both workflow runs passed,
- any image URL that still fails,
- the list of repos you suggest archiving or making private,
- and remind me to do this by hand (GitHub has no API for it): on my profile click **Customize your pins**, unpin the `awesome-chatgpt-prompts` fork, and pin my best real repos until the new voice-AI repos exist.
