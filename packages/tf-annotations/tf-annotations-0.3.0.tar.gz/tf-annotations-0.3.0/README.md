# code-annotations

This project was created as a way of creating a central "annotation" file of all the useful
notes that might be created in a code base such as `TODO` comments.

## Configuration

The project can be configured via a TOML file which by default is called `.tf-annotations.toml` but can be override with the `--config` flag.

Below is an example which can be found at `.tf-annotations-example.toml`

```TOML
title = "Code Annotation Config file"

file_suffix=["*.tf"]
headers=["TODO","KNOWISSUES"]
output_file="ANNOTATIONS.md"
comment_syntax = ["#", "//"]
```
