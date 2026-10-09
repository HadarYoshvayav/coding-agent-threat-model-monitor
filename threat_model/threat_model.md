# Coding Agent Threat Model

## 1. Objective

Assess how coding agents with access to source code, local files, tools, and external services could introduce security risks, including through malicious or unexpected behavior.

## 2. System Model

Assume a coding agent can:

- Read and modify project files.
- Execute commands through available tools.
- Access resources permitted by its runtime environment.
- Interact with external services when network access is available.

Actual capabilities depend on the deployment configuration.

## 3. Security Objectives

- Prevent unauthorized access to sensitive information.
- Detect suspicious use of tools and permissions.
- Protect source code and development infrastructure.
- Distinguish malicious behavior from legitimate but unusual workflows.

## 4. Threat Scenarios

Scenarios to investigate:

1. Unauthorized access to secrets.
2. Potential data exfiltration.
3. Prompt injection through untrusted project content.
4. Unauthorized code modification.
5. Destructive actions against project resources.

## 5. Detection and Evaluation

For each scenario, document the attack path, observable signals, proposed controls, benign lookalikes, and limitations of available telemetry.

Detection rules will initially be evaluated using synthetic event data.

## 6. Limitations

Observed behavior does not, by itself, establish intent. Missing logs, incomplete context, and legitimate workflows can all affect detection accuracy.
