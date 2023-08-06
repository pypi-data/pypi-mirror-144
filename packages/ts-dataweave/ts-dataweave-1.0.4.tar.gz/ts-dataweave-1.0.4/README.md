# DataWeave Python Wrapper [![Build Status](https://travis-ci.com/tetrascience/ts-dataweave-python.svg?token=uzw5KFZps3QXT9bqRDHY&branch=main)](https://travis-ci.com/tetrascience/ts-dataweave-python)

Python wrapper around MuleSoft's DataWeave data transformation engine.

## Installation

Add this package to your project using `pip` or `pipenv`:

```sh
# using pip
pip install ts-dataweave

# using pipenv
pipenv install ts-dataweave
```

The post-install script will download and extract the correct DataWeave command-line binary from [MuleSoft's DataWeave CLI repository](https://github.com/mulesoft-labs/data-weave-native/).

## Usage

To use DataWeave, import `ts_dataweave`:

```python
import ts_dataweave
```

### ts_dataweave.run(_payload_, _script_, \[_timeout_\])

Runs a DataWeave script with the specified payloads. The input payloads and script are written to temporary files and then removed when the execution is complete.

The _payload_ parameter should be a dictionary of `ts_dataweave.Payload` instances with _string_ keys. The payloads will be added to DataWeave with the corresponding key as the name of the payload.

The _script_ parameter should be a _string_, _bytes_, or _file-like_ object containing the DataWeave script.

The _timeout_ parameter is optional and should be the number of seconds that the script is allowed to run before an error is raised. The default timeout is 30 seconds.

The `ts_dataweave.run()` function returns a _bytes_ object containing the output of the DataWeave script execution.

> A _bytes_ object can easily be converted to a UTF-8 string by using `.decode("utf-8")`.

### ts_dataweave.Payload

The `dataweave.Payload` object contains information about a DataWeave payload. Use the constructor:

```py
ts_dataweave.Payload([payloadType], data)
```

The _payloadType_ parameter should be either `"json"`, `"csv"`, or `"xml"`. Alternatively, the members from the enumeration `dataweave.PayloadType` can also be used. Additional input types are not recognized at this time. If the _payloadType_ parameter is omitted, the type will be guessed based on the first non-whitespace byte of _data_:
  - `b"{"` ➡️ `"json"`
  - `b"["` ➡️ `"json"`
  - `b"<"` ➡️ `"xml"`
  - Else ➡️ `"csv"`
If the payload is large or there is any chance of ambiguity, please specify _payloadType_.

The _data_ parameter should be a _string_, _bytes_, _dict_, _list_, or _file-like_ object containing the content of the payload. The _payloadType_ parameter can be safely omitted if _data_ is a _dict_ or _list_.

## Examples

Example with explicit payload types:

```python
import ts_dataweave

print(ts_dataweave.run({
    "doc1": ts_dataweave.Payload(
        "xml", # can also use ts_dataweave.XML
        """<root>
            <firstname>Mike</firstname>
            <lastname>Foo</lastname>
        </root>"""
    ),
    "doc2": ts_dataweave.Payload(
        "json", # can also use ts_dataweave.JSON
        """{
            "birthday": "yesterday",
            "favoriteFood": "salami"
        }"""
    ),        
}, """contact: {
    firstname: doc1.root.firstname,
    lastname: doc1.root.lastname,
    food: doc2.favoriteFood,
    bday: doc2.birthday
}""").decode("utf-8"))
```

Payload data types can also be auto-detected:

```python
import ts_dataweave

print(ts_dataweave.run({
    "doc1": ts_dataweave.Payload(
        """<root>
            <firstname>Mike</firstname>
            <lastname>Foo</lastname>
        </root>"""
    ),
    "doc2": ts_dataweave.Payload(
        """{
            "birthday": "yesterday",
            "favoriteFood": "salami"
        }"""
    ),        
}, """contact: {
    firstname: doc1.root.firstname,
    lastname: doc1.root.lastname,
    food: doc2.favoriteFood,
    bday: doc2.birthday
}""").decode("utf-8"))
```

Python `dict`s and `list`s can also be used for payload data with payload type safely omitted:

```python
import ts_dataweave

print(ts_dataweave.run({
    "doc1": ts_dataweave.Payload(["Mike", "Foo"]),
    "doc2": ts_dataweave.Payload(
        {
            "birthday": "yesterday",
            "favoriteFood": "salami"
        }
    ),        
}, """contact: {
    firstname: doc1[0],
    lastname: doc1[1],
    food: doc2.favoriteFood,
    bday: doc2.birthday
}""").decode("utf-8"))
```

## Tests

The repository includes a test suite.

```sh
python -m pytest
```

## Compatibility

This package has been specifically developed and tested with Python 3.7 on Darwin (macOS) x86_64 and Linux x86_64 platforms.

## Changelog

### 1.0.4

- Update DataWeave CLI to v1.0.16 for macOS and Linux.

### 1.0.3

- Optional auto-detection of _payloadType_ in `ts_dataweave.Payload` constructor

### 1.0.2

- Fix wrapping of `ts_dataweave.Error` with another `ts_dataweave.Error`
- Sanitize payload IDs before executing DataWeave

### 1.0.1

- Use temporary file to capture DataWeave output instead of the standard output stream.

### 1.0.0

- Initial implementation.