# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - 2022-03-30
### Added
- CLI '-o' flag for specifying output file for results
- CLI '-n' flag for disabling results output
- Better logging framework with python's logging module
- Remade CLI '-l' flag to customize logging by pointing out a YAML conf file
- Write actual test case results to file (not just test case feedback data)
- Oracles can request a holdoff if they are unable to operate properly
- Dry runs in session if holdoffs are requested or testcases are going wrong
- Reference service using psutil
- Feedback loop based on grpc oracle observations
- CLI flag '-u' for disabling feedback loop
- Log probabilistic weights to results database to see change over time
- Plugin architecture for courier and grammar
- CLI flag '-C' to specify a session configuration file
- Removed '-i' flag, no longer used. Use '-C' instead

### Changed
- 'logger' module now renamed to 'results_db' to better reflect its use
- CLI '-l' flag removed in favor of '-o' and '-n' flags
- Removed some package-wide constants that didn't have to be package-wide
- Old debug printouts replaced by logging module

### Fixed

## [0.2.0] - 2022-01-18
### Added
- Get feedback data about the SUT via a gRPC interface
- Log test cases to file
- qwilfish-service, a simple gRPC service for monitoring the SUT
- qwilfish-simple-client, a gRPC client used for testing and development

### Changed
- Refactored sockets to make for easier Windows support in the (far) future
- Renamed runner class to courier
- "log" argument renamed to "debug" to avoid confusion with log file feature
- Refactored grammar and its annotations
- Created a "session" module instead of running things directly in "main"
- Minor changes to help text

### Fixed
- Missing copyright notice in license file

## [0.1.2] - 2021-12-07
### Fixed
- No Python commands in GitLab's CI/CD when publishing the release on GitLab

## [0.1.1] - 2021-12-07
### Fixed
- No changes, just bumping the patch number to avoid conflicts in TestPyPI

## [0.1.0] - 2021-12-07
### Added
- Linux support
- Generate LLDP frames with the three mandatory TLVs
- Specify how many frames to generate using the CLI
- Specify what network device to transmit on using the CLI
- Turn logging on/off using the CLI
- Support for probabilistic generation of LLDP frames
