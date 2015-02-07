# CivOmega: Question Module Boilerplate

This is a dummy module for [CivOmega](https://github.com/CivOmega/civomega). CivOmega Modules are what connect datasets and APIs to question patterns.

Note: This repository is where you should start if you want to allow people to ask questions about a dataset or API that doesn't exist in CivOmega already.  If you're actually interested in adding more questions to a dataset that already exists, we suggest that you contribute to an existing module instead of creating a new one from the ground up.

Modules have the following components:

- [parsers.py](comod_example/parser.py) - this is where you define question routes and answer logic
- [patterns.py](comod_example/patterns.py) - this is where you define the list of question patterns that your module knows how to answer
- [templates](comod_example/templates) - this is where you define the output format for your answers

## Creating a Module

### Step 1: Fork, Clone, and Configure

To build a module you first need to create a working version of [CivOmega](https://github.com/CivOmega/civomega) set up on your development environment.  Once this is done:

1. Fork this repository
2. Rename your copy from `civomega-mod-example` to `civomega-mod-meaningful-name`
3. Clone your fresh module into the `src` directory of your CivOmega installation
4. Rename your root directory from `comod_example` to `comod_meainingful_name`.
5. Rename the directory under templates in the same way.
6. Update `CIVOMEGA_MODULES` in settings.py to include your module's `comod_meaningful_name` (as defined in step 4)

### Step 2: Define Patterns

In `comod_example/patterns.py` you must define `PATTERNS` to contain a list of question patterns (strings) that your module knows how to answer.  These patterns should have "blanks" which will allow users to enter whatever information they would like. 

Wrap "blanks" in {braces}, and keep in mind that the content inside the braces dictate the type of object being entered.  This content should be lowercase, underscore_separated.

For example:

```
PATTERNS = frozenset([
	"how much money did {organization} donate in {year}",
    "is {person} a {thing}?",
    "is {person} a {thing} in {place}?",
])
```

You can create multiple categories of pattern as well, if your module knows how to answer more than one type of question.  See the [Sunlight bill module](https://github.com/CivOmega/civomega-mod-sunlightbills) for an example of this type of behavior.

### Step 3: Re-run CivOmega Migrations

Every time you define new patterns, you will have to refresh CivOmega's known pattern list.  When you're ready to test your module, you will need to run:

```shell
python manage.py update_patterns
python manage.py runserver
```