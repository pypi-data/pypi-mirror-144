# Changelog

## [Unreleased][]

[Unreleased]: https://github.com/chaostoolkit/chaostoolkit-dynatrace/compare/0.2.0...HEAD

## [0.2.0][] - 2022-03-29

[0.2.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-dynatrace/compare/0.1.0...0.2.0


### Added

* Probes to query metris v2 endpoint
* Add a control to send logs
* Correlate logs to traces from Open Telemtry if found
* Probes to query logs
* Using `black` as formatter of the code
* Brought handy makefile from other projects

### Changed

* Switched to [httpx][] as HTTP client
* Update github build
* Requires now Python 3.7 in line with Chaos Toolkit

[httpx]: https://www.python-httpx.org/

## [0.1.0][] - 2020-12-14

[0.1.0]: https://github.com/chaostoolkit-incubator/chaostoolkit-dynatrace/tree/0.1.0

### Added

-   Initial release
-   Added package to get failure rate service from dynatrace tools
