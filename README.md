# CivOmega: Department of Labor Search Module

A simple module for [CivOmega][civomega_repo]. See
[the CivOmega repo][civomega_repo].

* **CivOmega Demo**: http://www.civomega.com/
* **CivOmega Repo**: https://github.com/CivOmega/civomega

[civomega_repo]: https://github.com/CivOmega/civomega

---

This module queries the [Department of Labor](http://developer.dol.gov/)'s
APIs. When using this module (**note: it's installed in CivOmega by default**)
you'll need to have an API key.

Once you have the API key, make sure you do this…

```shell
export DOL_API_KEY=$YOUR_KEY_HERE
```

…before running the CivOmega server (`python manage.py runserver`).
