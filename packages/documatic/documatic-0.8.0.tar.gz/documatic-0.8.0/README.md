# Automated Documentation

This project is in a private beta.
for more information on using the tool,
to provide feedback,
or request access for a friend or colleague,
contact the beta runners.
**N.b.** this project calls an AWS API
with snippets of code
in order to generate documentation.
No code is stored.
Only your API key and a hash of your project name,
for the purposes of identifying usage,
are logged.

Documatic detects important information
about your project,
highlights important scripts,
functions and classes,
and summarises bits of code.
See the [featureset](#featureset)
for information on what is supported.
**N.b**
Some users have AI-aided code summarisation
activated,
however that is not the default behaviour.
If you would like to AI-aided summarisation,
please contact the team
(currently Python support only).
If you do not have AI-aided summarisation,
the tool fallsback to reading existing docstrings.
If you have a small python project
(a few functions),
all functions will be summarised.
We are working on improve our coverage
for functions and classes
so that useful documentation is generated for all.
If you have questions about the docs generated for your project,
please email `info@documatic.com` with a link to your codebase
and your generated docs attached.

## Get started

### Requirements

* `python 3.8` or greater
* `pip install documatic`
* In the base directory of your project, create a `.documatic.ini` config file
* Run `documatic-init` in a terminal in your project's base directory to generate a template config
* Documatic API key

#### Config file

##### pyproject.toml (preferred)

Configure `documatic`
in your pyproject.toml file
under a `[tool.documatic]` section.
It can have the following fields

| Field | Purpose | Required | Default |
:------|:--------|:---------|:--------|
| name | Project name | Y | - |
| description | Short description of the project | N | "SHORT PROJECT DESCRIPTION" |
| srcdir | Path to source code directory from the project root | Y | - |
| package | Name of the project codebase as imported in files (if not using local imports) | N | `srcdir` |
| local | For development purposes only. If `true`, uses local server for testing | N | `false` |
| docdir | Path to the folder in which generated docs should be saved. `.` is project root | Y | - |
| docname | Name of the document to be generated. ".md" file suffix will be added if not present | N | technical_doc.md |

**Note: strings in toml files must be wrapped in quotes.**
E.g.:

```
[tool.documatic]
name = "documatic"
srcdir = "documatic"
docdir = "docs/"
docname = "README.md"
```

##### .documatic.ini

Instead of a pyproject.toml, you can use a `.documatic.ini` file.

`.documatic.ini` can have the following fields:

| Header | Field | Purpose | Required | Default |
|:-------|:------|:--------|:---------|:--------|
| project | name | Project name | Y | - |
| project | description | Short description of the project | N | "SHORT PROJECT DESCRIPTION" |
| project | srcdir | Path to source code directory from the project root | Y | - |
| project | package | Name of the project codebase as imported in files (if not using local imports) | N | `srcdir` |
| project | local | For development purposes only. If `true`, uses local server for testing | N | `false` |
| project | language | The predominant codebase language | N | python |
| docs | docdir | Path to the folder in which generated docs should be saved. `.` is project root | Y | - |

An example `.documatic.ini` is:

```
[project]
name = MyCoolProject
language = python
srcdir = src/cool
package = cool

[docs]
docdir = .
```

#### API Key

To get full functionality of `documatic`,
a (free) API key is needed.
If you have been invited to join
the private beta,
your coordinator will provide
an API key for
and your team members
to use.
To setup your API key,
create a `.env` file in your project root
and give it the following fields.

```
DOCUMATIC_API_KEY = <YOUR-API-KEY>
```

**IMPORTANT: DO NOT ADD `.env` TO SOURCE CONTROL. YOUR API KEY MUST REMAIN PRIVATE.**
When `documatic` reads your config file,
it uses `python-dotenv` to read environment variables
from the `.env` file.

### Generate documentation

**Via CLI:**

The documatic package provides
a number of command line arguments:

| Command | Purpose |
|:--------|:--------|
| `documatic` | Generates/updates technical documentation |
| `documatic code` | Updates code snippets in technical documentation |
| `documatic changelog` | Generates a changelog/release notes |
| `documatic api` | Generate documentation for the API created by your project, if applicable (only **FastAPI** currently supported) |

To run one of the commands:

1. Open a terminal/command prompt
2. Navigate to the root directory of your project
3. Ensure you have the correct configuration and API key setup
4. Run your command of choice

**VSCode:**

There is a VSCode extension for this tool.
Search for `documatic` in the marketplace.
The extension comes with additional features
for streamlining your entire documentation generation process.

## Concepts

### Doc comments

Documatic adds markdown comments to technical documentation
to signal the start
and end
of different sections,
to help you curate automated technical documentation.
For example
```
<!---Documatic-section-code: e22c5ecb-myproj/folder/file.py-20-25--->
```
tells Documatic that the following bit of documentation
is a code snippet
and gives some information on when it was generated.
If that snippet of code is updated over time,
Documatic will automatically track that code
and update the snippet.

### Fixed document sections

Have a bit of documentation
which isn't autogenerated by Documatic?
Wrap the section in comments:

```
<!---Documatic-section-fixed: <position><number>-start--->
Bit of documentation to fix in place.
Maybe add your logo here,
or a markdown badge?
<!---Documatic-section-fixed: <position><number>-end--->
```

Where `<position>` is `top` to fix the section to the top
of the document
and `bottom` to fix it to the bottom,
and `<number>` is the order within the fixed sections.
E.g. `<!---Documatic-section-fixed: top1-start--->`
would fix some documentation to the very top
of the document.

## Featureset

Our current features
and short-term roadmap.

### Environment

* [X] requirements.txt
* [X] environment.yml
* [X] setup.py
* [X] setup.cfg
* [ ] pyproject.toml
* [ ] tox.ini

### Summarisation

* [X] AI-aided function summarisation
* [ ] AI-aided class summarisation (coming soon!)
* [X] Docstring + AI summarisation 

### Misc

* [X] Environment variables
* [X] REST requests
* [X] AWS calls (e.g. boto3)
* [X] MongoDB
* [X] FastAPI
* [X] Flask
* [ ] Celery
* [ ] Click (CLI)

#### Important code

`Documatic` tries to infer
what bits of code are important enough to document.
It does this in a number of ways:
* Imports into a top-level `__init__` or `__main__`
* A `if __name__ == "__main__"` script entrypoint
* Inherited class structure
* Classes used as type hints in functions

If no bits of code are identified as "important"
in your codebase,
please contact `info@documatic.com`
with details
so we can improve the tool
to work better with your code.

## License

You may download this package via pip
and use as intended,
**but you may not copy,
share
or edit the code**.
This is signified by the lack of specific license attached to the codebase.

## Development - Get started

### Requirements

- Developed with `python 3.9`
- `pip install -r requirements.txt`
- `pip install -r requirements-dev.txt`
- `pip install -e .`


In `.documatic.ini` add the following tags:

```
[project]
...
local = true
...
```

This will call `localhost` instead of the hosted server.
In a separate terminal,
run the web app locally in order to connect.

## Style Guide

- Use `black` to format code
- Other than `black` niches, adhere to PEP
- Use `isort` to sort imports
- Use numpy-style docstrings
- Use type hints and verify with `mypy`

### Testing

| CI | Purpose |
|:--:|:--------|
| `.github/workflows/test.yml` | Run linting and unit tests. Executes on all pull request branches |

Testing performed with `pytest`.
Run `pytest tests/unit`
to run unit tests.
There are integration tests
which should be run with a local API app running.
