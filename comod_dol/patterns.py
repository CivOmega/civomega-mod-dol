"""
contains `PATTERNS`, defining strings that this module may respond to
you can set anything you want here (which you can use in `parser.py`,
but you must set `PATTERNS`)
"""

# patterns for returning info about bills in congress
DOL_AGENCY_PATTERNS = frozenset([
    "What agencies are part of the Department of Labor"
])

LABOR_VIOLATION_PATTERNS = frozenset([
	"Who has violated child labor laws in {city}"
])

# IMPORTANT:
#   * all questions must be unique (you can change the variable inside
#     the pattern if the wording is otherwise identical)
#   * the variable must be unique inside the question (you can't have
#     "what are {person} and {person} talking about" but you can have
#     "what are {person1} and {person2} talking about")

PATTERNS = DOL_AGENCY_PATTERNS | LABOR_VIOLATION_PATTERNS