Version control systems such as Git are widely used in software development.

State two advantages of using version control when writing software. Explain each point from:

- the perspective of an individual programmer;
- the perspective of working in a team developing software.

State one disadvantage of Git. You can write this from either:

- your own perspective;
- the perspective of a new programmer who has just been introduced to it.

You may use external resources to help you, but answers must be written in your own words.

---

Advantages:
- branches
- blame

Disadvantages:
- No Bug reporting/Issues

Git branches allows a single developer to make different versions of their code with different features. Commits from one branch can also be cherry-picked between branches. This allows multiple full feature sets to be constantly improved. The developer can checkout between them and edit them seperately.
Branches are also helpful for teams. Multiple people can make a branch at one point in the commit history, work on it then merge it back into main. This is one of the most common ways programmers work as a team. Using branches means people are not working on the same history at once, only having to manage conflicts once when merging.

Git blame shows a file with information about which commit edited each line, who did that commit, and when. This means a solo developer can see when a change was made, and thus which other changes where made at a similar time. This can be a helpful way of viewing edit history for a specific file.
It's also used by teams of programmers to see who did which changes. They can then communicate about the file and lines changed, and any issues.