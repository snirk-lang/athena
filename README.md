# Athena

![Athenabot user icon][icon]

Source code of [Athenabot][athenabot], a GitHub bot which runs automation for
[Snirk][snirk] projects.

## Responsibilities

Athena runs some extra checks in Travis CI and comments on issues on Snirk's
GitHub.
Athena is inspired by the various bots which run on [Rust][rust].

- Categorizing GitHub issues and moving along the proposal process
- Assigning team members to issues based on experience and code affected
- Checking that pull requests match contributor guidelines
- Reporting extra information from CI builds and test results
- Running extended tests of the compiler and standard library
- Preparing deploys to GitHub and crates.io

## Icon

The icon for the GitHub bot is the Pallas Athena statue in front of the Austrian
Parliament building.
The image  was taken from [this wikimedia image][source] and modified
(cropping and color adjustment).

We release the image under the same GNU Free Documentation and Creative Commons
share-alike licenses as the original image was licensed under.

[athenabot]: https://github.com/apps/athenabot
[snirk]: https://github.com/snirk-lang
[icon]: https://avatars2.githubusercontent.com/in/14194?s=240&u=e75ab45907d017c755d2c04c51f635ed3054d3e3
[source]: https://commons.wikimedia.org/wiki/File:Wien_-_Athene_3_Kopf.jpg
[rust]: https://github.com/rust-lang/
