# Chaos Toolkit extension for Dynatrace

![Build](https://github.com/chaostoolkit-incubator/chaostoolkit-dynatrace/workflows/Build/badge.svg)

[Dynatrace][dynatrace] support for the [Chaos Toolkit][chaostoolkit].

[dynatrace]: https://www.dynatrace.es/
[chaostoolkit]: http://chaostoolkit.org/

## Install

To be used from your experiment, this package must be installed in the Python
environment where [chaostoolkit][] already lives.

[chaostoolkit]: https://github.com/chaostoolkit/chaostoolkit

```
$ pip install chaostoolkit-dynatrace
```

## Usage

To use this package, you must  have access to a Dynatrace instance via
[DynatraceApi][]  and be allowed to connect to it.

[DynatraceApi]: https://www.dynatrace.com/support/help/dynatrace-api/basics/dynatrace-api-authentication/

the access credentials to the api must be specified in the configuration section

```json
{

    "configuration": {
        "dynatrace_base_url": "https://{your-environment-id}.live.dynatrace.com"
    },
    "secrets": {
        "dynatrace": {
            "token": "..."
        }
    }
}
```

Here is an example of how to get the failure rate of a service in Dynatrace.
for this example, the api for validate de failure rate is [Metric-v1][mv1]

[mv1]:https://www.dynatrace.com/support/help/dynatrace-api/environment-api/metric-v1/


```json
{
    "type": "probe",
    "name": "get-failure-rate-services",
    "provider": {
        "type": "python",
        "module": "chaosdynatrace.timeseries.v1.probes",
        "func": "failure_rate",
        "secrets": ["dynatrace"],
        "arguments": {
            "entity": "SERVICE-665B05BC92550119",
            "relative_time": "30mins",
            "failed_percentage": 1
        }
    }
}
```

The probe returns `true` if the api request failure percentage is less than 
the `failed_percentage` value or return `false`.

The extension also exports a control to send events to Dynatrace. For instance:

```json
{
    "controls": [
        {
            "name": "dynatrace",
            "provider": {
                "type": "python",
                "secrets": ["dynatrace"],
                "module": "chaosdynatrace.events.v2.control"
            }
        }
    ]
}
```

This will send start/stop logs of the experiment events.

You can correlate them to traces using the [Open Telemetry][opentracing]
extension.

[opentracing]: https://chaostoolkit.org/drivers/opentracing/

```json
{
    "configuration": {
        "dynatrace_base_url": "https://{your-environment-id}.live.dynatrace.com",
        "tracing_provider": "opentelemetry",
        "tracing_opentelemetry_exporter": "oltp-http",
        "tracing_opentelemetry_collector_endpoint": "https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/traces",
        "tracing_opentelemetry_collector_headers": {
            "Authorization": "Api-Token <TOKEN>"
        }
    },
    "controls": [
        {
            "name": "opentracing",
            "provider": {
                "type": "python",
                "module": "chaostracing.control"
            }
        }
    ]
```

The logs and traces will be automatically correlated.

## Contribute

If you wish to contribute more functions to this package, you are more than
welcome to do so. Please, fork this project, make your changes following the
usual [PEP 8][pep8] code style, sprinkling with tests and submit a PR for
review.

[pep8]: https://pycodestyle.readthedocs.io/en/latest/

### Develop

If you wish to develop on this project, make sure to install the development
dependencies. But first, [create a virtual environment][venv] and then install
those dependencies.

[venv]: http://chaostoolkit.org/reference/usage/install/#create-a-virtual-environment

```console
$ pip install -r requirements-dev.txt -r requirements.txt 
```

Then, point your environment to this directory:

```console
$ pip install -e .
```

Now, you can edit the files and they will be automatically be seen by your
environment, even when running from the `chaos` command locally.

### Test

To run the tests for the project execute the following:

```
$ pytest
```
