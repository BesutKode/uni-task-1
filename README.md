# Elimination task 1

## Task

Find and fix technical bugs in translated messages hosted in GitHub repositories.

## Objective

This task assists participants gain an advanced understanding of
text markup and translation file formats, and open source quality
assurance tools available for those file formats.

DO NOT translate messages.  That is not the objective of this task.

## Warning

During the entire elimination phase, participants must not interact with a
GitHub repository that was selected by another participant for this task
until after the other participant has successfully completed this task.

Universitas participants may not select the following repositories
for this task, and should not interact with these repositories:

- https://github.com/phpmyadmin/localized_docs
- https://github.com/phpmyadmin/phpmyadmin
- https://gitlab.com/noosfero/noosfero (mirror at https://github.com/noosfero/noosfero)
- https://github.com/godotengine/godot
- https://github.com/exaile/exaile
- https://github.com/hangoutsbot/hangoutsbot-locales

## Steps

### Accept invite

You will receive an email from GitHub, inviting you to join the
GitHub BesutKode organisation.

You need to accept that invitation.

Once you have accepted that invitation, you will have "Write" access to
this repository:

https://github.com/BesutKode/uni-task-1

This repository is a private repository, *however*
it will be converted to a public repository on
30 October 2016.

Everything you do will be public forever.

DO NOT link to an Issue or Pull Request of another repository.

There is a "gitter" channel for this repository, only accessible by
successful participants of Besut Kode Universitas:

https://gitter.im/BesutKode/uni-task-1

This channel is private.

Behave professionally and collegially.

### Find 20 bugs in a translation project

DO NOT create an Issue in another repository for this task.

Bugs in translated messages include:

-  semantic problems, such as missing grammatical structure,
   like a missing period at the end of a sentence.

-  syntax errors, such as invariant parts of the source message
   that have been translated when they should not be translated.

There are existing open source tools that find and even fix
these problems automatically.  An example of an existing open source tool is
[`translate-toolkit`](https://en.wikipedia.org/wiki/Translate_Toolkit),
which is included in most Linux distributions.

On the repository wiki is a page "Existing tools", which has more
tools that may be useful.

It is recommended that you look for translation bugs in projects
that use a [Weblate](https://en.wikipedia.org/wiki/Weblate) service.
Weblate allows anyone to contribute translations that are
[lazy-committed](https://docs.weblate.org/en/latest/admin/continuous.html#lazy-commit)
to the repository.

If the weblate project is linked with a GitHub repository, the changes that are
made in the weblate service will appear on the GitHub profile of the person
who made the changes in weblate, *if* their email address in GitHub and weblate
are identical.

Some weblate services allow authentication using GitHub, which presets the
email address to be identical.

On the wiki is a page "Weblate" that contains more information about weblate
services.  Two of the largest weblate services containing many varied
projects connected to GitHub repositories are:

- https://hosted.weblate.org/
- https://l10n.opensuse.org/

Participants may select non-Weblate GitHub repositories.

### Register your project

Only one participant may work on a GitHub repository at a time.
This is to avoid multiple conflicting changes.

Each participant will create a page on the BesutKode repository wiki
about the repository they have selected and the bug(s) they have found.

Once you have found a project with technical bugs, first search the wiki
to check if someone else has already chosen the same repository.

If nobody else has already selected the same repository,
create a page on the wiki named with your GitHub username,
and include the following:

1. A link to the GitHub repository
2. A link to the translation project page (e.g. weblate service)
3. A technical description of the bug you have found
4. The command that you used to find the bugs
5. The output of the above command
6. Any other information you believe is relevant.

Writing in bahasa Indonesia is acceptable.

### Fix 20 or more bugs

Open Source projects using Weblate prefer that translations are provided
using Weblate, as it reduces the workload for the committers since Weblate
automatically commits changes.

However this task requires that you modify a large group of messages
that have a technical problem.  Technical fixes should ideally be submitted
via a Pull Request on the GitHub project, for peer-review.

However be aware that it is common for projects to refuse to accept
Pull Requests for translation files.

For example, openSUSE has indicated that they prefer translations via weblate.

Also some projects do not commit translations using the identity of the
translator.
For example, [SugarLabs projects](https://github.com/sugarlabs)
use a [Pootle](https://en.wikipedia.org/wiki/Pootle) service at
[translate.sugarlabs.org](https://translate.sugarlabs.org/)
to manage their translations, and they will reject changes to translation files
that are not performed in their Pootle service.
Then those translations from their Pootle service are committed by maintainers
in an adhoc manner.

For this task, it does not matter whether you use a Pull Request or use a
web translation service, as long as those changes appear on your GitHub
profile. (i.e. edits in a Pootle service will be ineligible)

If you did not find and fix 20 problematic messages in your first
registered repository, you may now select another repository on your wiki page,
and repeat until you have reached 20 fixed messages.

#### Example

The [sample task](https://wikimedia-id.github.io/besutkode/university-sample-task-1-en.html)
has some background about the phpMyAdmin localisation project.

The participants who completed that sample task can be seen at
[`id.po`](https://github.com/phpmyadmin/localized_docs/commits/master/po/id.po).

Examples of small fixes can also be seen there, such as:

- https://github.com/phpmyadmin/localized_docs/commit/9cc7914fe0ddc8caa90ca5da32150442de2561e4#diff-ef37f181f82218fc93bce3f96e620e4d
- https://github.com/phpmyadmin/localized_docs/commit/877c28f9f859a4806b1556764be697d0aab0501c#diff-ef37f181f82218fc93bce3f96e620e4d

An example of a Pull Request that you should achieve for this task is
[https://github.com/phpmyadmin/localized_docs/pull/2](https://github.com/phpmyadmin/localized_docs/pull/2)

### Find one more bug

Create or improve an Open Source program, in any programming language,
to detect at least one translation bug in the repository.

The detected problem must not be able to be detected by any of the existing tools.

If you modify an existing program, it is not necessary to submit your improvement
to the maintainers.  It can be a work in process.

If your program is only a small script, your may submit it as a pull request to
the BesutKode repository in a subdirectory named according to your GitHub username.

Add a brief explanation of your new tool to your wiki page.

## Assessment

When you believe you have finished, create an issue in the Besut Kode repository
assigned to @jayvdb.

The title of your issue should be your GitHub username, and the body
of you issue should be link to your wiki page.

DO NOT link to an Issue or Pull Request of another repository.

By default, the task is assessed by reviewing merged pull requests on your
GitHub profile to translation files.

For example, the following GitHub search query is used:

>  author:<username> is:pr is:merged created:>2016-10-19

The assessment will count messages modified, and manually checking
that the syntax was previously incorrect, and has been corrected by your
commit, without introducing new syntax errors.

If, and only if, the syntax of a message was previously incorrect,
the translation of the message may be improved if you *know* the language
of the message.

Also, the kind of error fixed in your commit should be completely removed
from the repository, unless your wiki page explicitly states why some
occurrences of the error were not fixed.

## Related StackOverflow tags

- [translate-toolkit](http://stackoverflow.com/questions/tagged/translate-toolkit)
- [weblate](http://stackoverflow.com/questions/tagged/weblate)
- [gettext](http://stackoverflow.com/questions/tagged/gettext)
- [reStructuredText](http://stackoverflow.com/questions/tagged/reStructuredText)
