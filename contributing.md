# Contribution Guidelines

This is a curated list of the best Mach projects, not a catalog of every one. [mach-ecosystem](https://github.com/briar-systems/mach-ecosystem) lists everything.

## What belongs here

- The project is written in or for Mach.
- It is public, maintained, and not archived.
- It has a README explaining what it does and how to use it.
- It is useful to other people, not just a personal experiment.

## Adding a project

- Open one pull request per project, titled `Add project-name`.
- Add it at the bottom of the category it fits. If no category fits, propose a new one in the same pull request and add it to `Contents`.
- Format it as `- [Name](link) - Description.` The description starts with an uppercase letter, ends with a period, and says what the project does without marketing language. Every entry is Mach, so leave out "for Mach".
- Run `npx awesome-lint` and fix what it reports. CI runs it too.

## Changing or removing a project

Open a pull request with the reason. Projects that are archived, abandoned, or broken get removed.
