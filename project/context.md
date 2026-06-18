# System Architecture Analysis
<!-- generated in 0.01s -->

## Overview

- **Project**: /home/tom/github/wronai/curllm
- **Primary Language**: python
- **Languages**: python: 516, shell: 28, yaml: 13, json: 5, javascript: 5
- **Analysis Mode**: static
- **Total Functions**: 2552
- **Total Classes**: 322
- **Modules**: 585
- **Entry Points**: 2043

## Architecture by Module

### static.js.app
- **Functions**: 189
- **File**: `app.js`

### extension.extension
- **Functions**: 109
- **Classes**: 2
- **File**: `extension.js`

### functions.js.extractors
- **Functions**: 34
- **File**: `extractors.js`

### functions.js.safety
- **Functions**: 30
- **Classes**: 2
- **File**: `safety.js`

### curllm_core.url_resolution.resolver
- **Functions**: 23
- **Classes**: 1
- **File**: `resolver.py`

### examples.api-clients.node_api_example
- **Functions**: 22
- **File**: `node_api_example.js`

### curllm_core.transparent.orchestrator
- **Functions**: 22
- **Classes**: 1
- **File**: `orchestrator.py`

### curllm_server.executor.curllm_executor
- **Functions**: 22
- **Classes**: 1
- **File**: `curllm_executor.py`

### examples
- **Functions**: 21
- **File**: `examples.py`

### scripts.dev_watcher
- **Functions**: 21
- **Classes**: 4
- **File**: `dev_watcher.py`

### curllm_core.streamware.components.curllm
- **Functions**: 21
- **Classes**: 2
- **File**: `curllm.py`

### curllm_core.streamware.components.form.smart_orchestrator.smart_form_orchestrator
- **Functions**: 21
- **Classes**: 1
- **File**: `smart_form_orchestrator.py`

### curllm_core.execution.executor.curllm_executor
- **Functions**: 21
- **Classes**: 1
- **File**: `curllm_executor.py`

### curllm_core.orchestrators.live
- **Functions**: 21
- **Classes**: 2
- **File**: `live.py`

### functions.patterns.registry
- **Functions**: 21
- **Classes**: 2
- **File**: `registry.py`

### curllm_core.llm_factory
- **Functions**: 19
- **Classes**: 4
- **File**: `llm_factory.py`

### curllm_core.element_finder.finder.llm_element_finder.llm_element_finder
- **Functions**: 19
- **Classes**: 1
- **File**: `llm_element_finder.py`

### curllm_core.orchestrators.master
- **Functions**: 19
- **Classes**: 3
- **File**: `master.py`

### curllm_logs.run_logger
- **Functions**: 18
- **Classes**: 1
- **File**: `run_logger.py`

### curllm_core.streamware.components.bql.parser
- **Functions**: 18
- **Classes**: 3
- **File**: `parser.py`

## Key Entry Points

Main execution flows into the system:

### curllm_core.execution.executor.curllm_executor.CurllmExecutor.execute_workflow
- **Calls**: curllm_core.runtime.parse_runtime_from_instruction, None.join, RunLogger, run_logger.log_heading, curllm_core.config_logger.log_all_config, cmd_parts.append, cmd_parts.append, cmd_parts.append

### curllm_core.form_fill.deterministic_form_fill
> Fill form using LLM-driven field detection.

Architecture:
1. LLM generates field concepts dynamically (if available)
2. Field concepts are passed to 
- **Calls**: curllm_core.form_fill.parser.parse_form_pairs, raw_pairs.items, selectors.get, selectors.get, isinstance, k.lower, field_concepts.items, page.evaluate

### curllm_core.running.runner.run_task
- **Calls**: None.lower, any, int, ToolRetryManager, range, run_logger.log_text, executor._open_page_with_prechecks, executor._parse_form_pairs

### curllm_core.multi_criteria_filter.MultiCriteriaFilter.filter_products
> Filter products using multi-criteria approach

Args:
    products: List of products from extraction
    instruction: User's original instruction
    u
- **Calls**: self.instruction_parser.parse, self._log, FilterStage, len, len, self.stages.append, any, self._log

### extension.extension.CurllmExtension.curllmExtension
- **Calls**: extension.extension.constructor, extension.extension.CurllmExtension.init, extension.extension.addListener, extension.extension.CurllmExtension.handleMessage, extension.extension.CurllmContentScript.injectHelpers, extension.extension.CurllmExtension.sendResponse, extension.extension.CurllmContentScript.getLocalStorage, extension.extension.CurllmContentScript.getSessionStorage

### curllm_core.navigation.open_page_with_prechecks
- **Calls**: runtime.get, bool, run_logger.log_kv, agent.browser.new_page, run_logger.log_kv, runtime.get, agent.browser.new_page, page.evaluate

### scripts.analyze_deps.main
- **Calls**: monitoring.website_monitor.print, monitoring.website_monitor.print, monitoring.website_monitor.print, monitoring.website_monitor.print, scripts.analyze_deps.find_python_files, set, sorted, monitoring.website_monitor.print

### curllm_core.deprecated.cli_orchestrator.main
- **Calls**: curllm_core.deprecated.cli_orchestrator.parse_args, OrchestratorConfig, monitoring.website_monitor.print, monitoring.website_monitor.print, monitoring.website_monitor.print, monitoring.website_monitor.print, monitoring.website_monitor.print, monitoring.website_monitor.print

### scripts.analyze_dependencies.main
- **Calls**: monitoring.website_monitor.print, monitoring.website_monitor.print, monitoring.website_monitor.print, monitoring.website_monitor.print, scripts.analyze_dependencies.build_dependency_graph, monitoring.website_monitor.print, monitoring.website_monitor.print, scripts.analyze_dependencies.analyze_llm_versions

### wordpress_batch.batch_create_posts
- **Calls**: CurllmExecutor, functions.registry.FunctionRegistry.list, monitoring.website_monitor.print, enumerate, monitoring.website_monitor.print, monitoring.website_monitor.print, monitoring.website_monitor.print, monitoring.website_monitor.print

### examples.streamware.streamware_quickstart.main
> Quick start examples
- **Calls**: monitoring.website_monitor.print, monitoring.website_monitor.print, monitoring.website_monitor.print, curllm_core.streamware.helpers.enable_diagnostics.enable_diagnostics, monitoring.website_monitor.print, monitoring.website_monitor.print, curllm_core.streamware.registry.list_available_components, monitoring.website_monitor.print

### examples.currency.currency_example.main
> Demonstrate currency translation for e-commerce extraction.
- **Calls**: monitoring.website_monitor.print, monitoring.website_monitor.print, monitoring.website_monitor.print, monitoring.website_monitor.print, monitoring.website_monitor.print, monitoring.website_monitor.print, monitoring.website_monitor.print, monitoring.website_monitor.print

### curllm_core.orchestration.orchestrator.orchestrator.Orchestrator._save_log_legacy
> Legacy log saving (fallback when package not available)
- **Calls**: logger.info, open, f.write, f.write, f.write, f.write, f.write, result.command.replace

### curllm_core.dom_toolkit.orchestrator.task_router.ExtractionOrchestrator.extract
> Main extraction pipeline with minimal LLM usage.

Args:
    page: Playwright page
    instruction: User's extraction instruction
    use_llm_selection
- **Calls**: self._log, task.get, task.get, self._log, self._log, self._log, self._log, self._log

### curllm_core.validation.task_validator.task_validator.task_validator.TaskValidator._validate_rules
> Validate against business rules
- **Calls**: instruction.lower, re.search, re.search, any, any, ValidationCheck, int, isinstance

### examples.detection.llm_heuristics_example.main
> Example: Discover heuristics for any e-commerce site
- **Calls**: monitoring.website_monitor.print, monitoring.website_monitor.print, monitoring.website_monitor.print, async_playwright, monitoring.website_monitor.print, monitoring.website_monitor.print, monitoring.website_monitor.print, monitoring.website_monitor.print

### curllm_core.server.proxy_health
> Check proxy health and optionally prune dead entries from registry.
Body JSON:
  - url: test URL (default: http://example.com)
  - timeout: seconds (d
- **Calls**: app.route, float, int, bool, functions.registry.FunctionRegistry.list, jsonify, request.get_json, data.get

### curllm_core.remediation.remediate_if_empty
- **Calls**: len, len, len, len, len, page_context.setdefault, None.update, curllm_core.human_verify.looks_like_human_verify_text

### curllm_core.cli.feedback.main
- **Calls**: argparse.ArgumentParser, parser.add_subparsers, subparsers.add_parser, rate_parser.add_argument, rate_parser.add_argument, rate_parser.add_argument, rate_parser.add_argument, rate_parser.add_argument

### captcha.playwright_bql_framework.BQLExecutor._run_action
- **Calls**: a.get, a.get, a.get, None.fill, ValueError, a.get, None.type, self.page.locator

### curllm_core.orchestration.orchestrator.orchestrator.Orchestrator.execute
> Execute a natural language command.

Args:
    command: Natural language command
    
Returns:
    OrchestratorResult with execution details
- **Calls**: datetime.now, start_time.strftime, self._log, self._log, OrchestratorResult, self._log, self.parser.parse, self._log

### curllm_core.iterative_extractor.IterativeExtractor.run
> Run full iterative extraction pipeline

Returns: {products: [...], metadata: {...}}
- **Calls**: self._extract_price_limit, self._validate_results, self.run_logger.log_text, self.run_logger.log_text, self.quick_page_check, quick_check.get, quick_check.get, self.detect_container_structure

### curllm_core.url_resolution.resolver.UrlResolver.resolve
> Resolve URL to match user intent.

Args:
    url: Original URL provided by user
    instruction: User's task instruction
    max_attempts: Maximum nav
- **Calls**: self._log, self._log, self.detect_goal, self._log, steps.append, self._log, ResolvedUrl, self._analyze_page_match

### curllm_core.url_resolver_llm.LLMUrlResolver._find_candidates
> Use atomic DOM functions to find link candidates.
Uses dom_helpers module for efficient, reusable operations.
- **Calls**: criteria.get, criteria.get, criteria.get, candidates.sort, set, sorted, self._atomic_extract_links, None.lower

### pricing.app.api_compare_stream
> Streaming API endpoint for price comparison with real-time logs.

Uses Server-Sent Events (SSE) to stream progress updates.
- **Calls**: app.route, request.get_json, data.get, data.get, data.get, data.get, Response, pricing.app.get_comparator

### curllm_core.orchestration.orchestrator.orchestrator.Orchestrator._execute_with_captcha_handling
> Execute plan in visible mode with CAPTCHA handling.

Opens visible browser, navigates to form, and waits for user
to solve CAPTCHA before continuing.
- **Calls**: OrchestratorResult, self._log, enumerate, self._log, self._log, self._log, self._log, self._log

### curllm_core.orchestrators.live.LiveInteractionOrchestrator._parse_single_action
> Parse a single action from text
- **Calls**: None.strip, re.search, re.search, re.search, re.search, re.search, re.search, re.search

### captcha.allegro_captcha_solver.main
> Główna funkcja - przykład użycia
- **Calls**: monitoring.website_monitor.print, monitoring.website_monitor.print, AllegroSlidingPuzzleSolver, async_playwright, monitoring.website_monitor.print, monitoring.website_monitor.print, monitoring.website_monitor.print, p.chromium.launch

### curllm_core.wordpress.WordPressAutomation._create_gutenberg_post
- **Calls**: self.page.locator, content.split, title_input.first.click, title_input.first.fill, self.page.keyboard.press, paragraph.strip, self.page.locator, self.run_logger.log_text

### curllm_core.planner_progress.progress_tick
- **Calls**: page_context.get, page_context.get, len, len, int, page_context.get, page_context.get, min

## Process Flows

Key execution flows identified:

### Flow 1: execute_workflow
```
execute_workflow [curllm_core.execution.executor.curllm_executor.CurllmExecutor]
  └─ →> parse_runtime_from_instruction
  └─ →> log_all_config
      └─> get_all_config_variables
          └─ →> str
```

### Flow 2: deterministic_form_fill
```
deterministic_form_fill [curllm_core.form_fill]
  └─ →> parse_form_pairs
```

### Flow 3: run_task
```
run_task [curllm_core.running.runner]
```

### Flow 4: filter_products
```
filter_products [curllm_core.multi_criteria_filter.MultiCriteriaFilter]
```

### Flow 5: curllmExtension
```
curllmExtension [extension.extension.CurllmExtension]
  └─> init
      └─> checkServerStatus
          └─> setIcon
          └─> showNotification
  └─> handleMessage
      └─> executeAutomation
          └─> captureTabSession
      └─> sendResponse
  └─ →> injectHelpers
```

### Flow 6: open_page_with_prechecks
```
open_page_with_prechecks [curllm_core.navigation]
```

### Flow 7: main
```
main [scripts.analyze_deps]
  └─> find_python_files
  └─ →> print
  └─ →> print
```

### Flow 8: batch_create_posts
```
batch_create_posts [wordpress_batch]
  └─ →> list
  └─ →> print
  └─ →> print
```

### Flow 9: _save_log_legacy
```
_save_log_legacy [curllm_core.orchestration.orchestrator.orchestrator.Orchestrator]
```

### Flow 10: extract
```
extract [curllm_core.dom_toolkit.orchestrator.task_router.ExtractionOrchestrator]
```

## Key Classes

### extension.extension.CurllmContentScript
- **Methods**: 63
- **Key Methods**: extension.extension.CurllmContentScript.init, extension.extension.CurllmContentScript.handleMessage, extension.extension.CurllmContentScript.sendResponse, extension.extension.CurllmContentScript.sendResponse, extension.extension.CurllmContentScript.sendResponse, extension.extension.CurllmContentScript.sendResponse, extension.extension.CurllmContentScript.sendResponse, extension.extension.CurllmContentScript.sendResponse, extension.extension.CurllmContentScript.getLocalStorage, extension.extension.CurllmContentScript.key

### extension.extension.CurllmExtension
- **Methods**: 46
- **Key Methods**: extension.extension.CurllmExtension.init, extension.extension.CurllmExtension.checkServerStatus, extension.extension.CurllmExtension.response, extension.extension.CurllmExtension.data, extension.extension.CurllmExtension.setupListeners, extension.extension.CurllmExtension.handleMessage, extension.extension.CurllmExtension.result, extension.extension.CurllmExtension.sendResponse, extension.extension.CurllmExtension.sendResponse, extension.extension.CurllmExtension.workflow

### curllm_core.url_resolution.resolver.UrlResolver
> Smart URL resolver that validates and corrects URLs based on user intent.

Usage:
    resolver = Url
- **Methods**: 22
- **Key Methods**: curllm_core.url_resolution.resolver.UrlResolver.__init__, curllm_core.url_resolution.resolver.UrlResolver.detect_goal, curllm_core.url_resolution.resolver.UrlResolver._detect_goal_fallback, curllm_core.url_resolution.resolver.UrlResolver._normalize_polish, curllm_core.url_resolution.resolver.UrlResolver.find_cart_url, curllm_core.url_resolution.resolver.UrlResolver.find_contact_url, curllm_core.url_resolution.resolver.UrlResolver.find_login_url, curllm_core.url_resolution.resolver.UrlResolver.find_generic_url, curllm_core.url_resolution.resolver.UrlResolver._llm_find_link, curllm_core.url_resolution.resolver.UrlResolver.find_url_for_goal

### curllm_core.transparent.orchestrator.TransparentOrchestrator
> Orkiestrator z pełną transparentnością dla LLM.
LLM widzi każdą decyzję i może ją modyfikować.
- **Methods**: 22
- **Key Methods**: curllm_core.transparent.orchestrator.TransparentOrchestrator.__init__, curllm_core.transparent.orchestrator.TransparentOrchestrator.log, curllm_core.transparent.orchestrator.TransparentOrchestrator.add_decision, curllm_core.transparent.orchestrator.TransparentOrchestrator._get_timestamp, curllm_core.transparent.orchestrator.TransparentOrchestrator.orchestrate_form_fill, curllm_core.transparent.orchestrator.TransparentOrchestrator._phase1_field_mapping, curllm_core.transparent.orchestrator.TransparentOrchestrator._create_mapping_prompt, curllm_core.transparent.orchestrator.TransparentOrchestrator._parse_mapping_response, curllm_core.transparent.orchestrator.TransparentOrchestrator._phase2_verify_mapping, curllm_core.transparent.orchestrator.TransparentOrchestrator._verify_fields_in_dom

### curllm_server.executor.curllm_executor.CurllmExecutor
> Main browser automation executor with LLM support
- **Methods**: 22
- **Key Methods**: curllm_server.executor.curllm_executor.CurllmExecutor.__init__, curllm_server.executor.curllm_executor.CurllmExecutor._setup_llm, curllm_server.executor.curllm_executor.CurllmExecutor.execute_workflow, curllm_server.executor.curllm_executor.CurllmExecutor._create_agent, curllm_server.executor.curllm_executor.CurllmExecutor._setup_browser, curllm_server.executor.curllm_executor.CurllmExecutor._setup_playwright, curllm_server.executor.curllm_executor.CurllmExecutor._setup_browserless, curllm_server.executor.curllm_executor.CurllmExecutor._take_screenshot, curllm_server.executor.curllm_executor.CurllmExecutor._extract_page_context, curllm_server.executor.curllm_executor.CurllmExecutor._generate_action

### curllm_core.streamware.components.form.smart_orchestrator.smart_form_orchestrator.SmartFormOrchestrator
> Intelligent form filling orchestrator with LLM verification.

Workflow:
1. Detect form fields and ty
- **Methods**: 21
- **Key Methods**: curllm_core.streamware.components.form.smart_orchestrator.smart_form_orchestrator.SmartFormOrchestrator.__init__, curllm_core.streamware.components.form.smart_orchestrator.smart_form_orchestrator.SmartFormOrchestrator._log, curllm_core.streamware.components.form.smart_orchestrator.smart_form_orchestrator.SmartFormOrchestrator._log_json, curllm_core.streamware.components.form.smart_orchestrator.smart_form_orchestrator.SmartFormOrchestrator.orchestrate, curllm_core.streamware.components.form.smart_orchestrator.smart_form_orchestrator.SmartFormOrchestrator._detect_fields, curllm_core.streamware.components.form.smart_orchestrator.smart_form_orchestrator.SmartFormOrchestrator._smart_map_fields, curllm_core.streamware.components.form.smart_orchestrator.smart_form_orchestrator.SmartFormOrchestrator._fallback_mapping, curllm_core.streamware.components.form.smart_orchestrator.smart_form_orchestrator.SmartFormOrchestrator._compute_field_match_score, curllm_core.streamware.components.form.smart_orchestrator.smart_form_orchestrator.SmartFormOrchestrator._are_semantically_related, curllm_core.streamware.components.form.smart_orchestrator.smart_form_orchestrator.SmartFormOrchestrator._fill_with_verification

### curllm_core.execution.executor.curllm_executor.CurllmExecutor
> Main browser automation executor with LLM support
- **Methods**: 21
- **Key Methods**: curllm_core.execution.executor.curllm_executor.CurllmExecutor.__init__, curllm_core.execution.executor.curllm_executor.CurllmExecutor._setup_llm, curllm_core.execution.executor.curllm_executor.CurllmExecutor.execute_workflow, curllm_core.execution.executor.curllm_executor.CurllmExecutor._create_agent, curllm_core.execution.executor.curllm_executor.CurllmExecutor._setup_browser, curllm_core.execution.executor.curllm_executor.CurllmExecutor._execute_task, curllm_core.execution.executor.curllm_executor.CurllmExecutor._take_screenshot, curllm_core.execution.executor.curllm_executor.CurllmExecutor._extract_page_context, curllm_core.execution.executor.curllm_executor.CurllmExecutor._generate_action, curllm_core.execution.executor.curllm_executor.CurllmExecutor._execute_action

### curllm_core.orchestrators.live.LiveInteractionOrchestrator
> Specialized orchestrator for real-time GUI interactions.

Features:
- Natural language to action tra
- **Methods**: 21
- **Key Methods**: curllm_core.orchestrators.live.LiveInteractionOrchestrator.__init__, curllm_core.orchestrators.live.LiveInteractionOrchestrator.orchestrate, curllm_core.orchestrators.live.LiveInteractionOrchestrator._parse_actions, curllm_core.orchestrators.live.LiveInteractionOrchestrator._parse_single_action, curllm_core.orchestrators.live.LiveInteractionOrchestrator._parse_with_llm, curllm_core.orchestrators.live.LiveInteractionOrchestrator._execute_action, curllm_core.orchestrators.live.LiveInteractionOrchestrator._do_click, curllm_core.orchestrators.live.LiveInteractionOrchestrator._do_double_click, curllm_core.orchestrators.live.LiveInteractionOrchestrator._do_right_click, curllm_core.orchestrators.live.LiveInteractionOrchestrator._do_hover

### curllm_core.element_finder.finder.llm_element_finder.llm_element_finder.LLMElementFinder
> Use LLM to find elements on page based on intent.

Instead of hardcoding selectors like:
    'input[
- **Methods**: 19
- **Key Methods**: curllm_core.element_finder.finder.llm_element_finder.llm_element_finder.LLMElementFinder.__init__, curllm_core.element_finder.finder.llm_element_finder.llm_element_finder.LLMElementFinder.get_page_context, curllm_core.element_finder.finder.llm_element_finder.llm_element_finder.LLMElementFinder.find_element, curllm_core.element_finder.finder.llm_element_finder.llm_element_finder.LLMElementFinder.find_form_field, curllm_core.element_finder.finder.llm_element_finder.llm_element_finder.LLMElementFinder.find_submit_button, curllm_core.element_finder.finder.llm_element_finder.llm_element_finder.LLMElementFinder.find_search_input, curllm_core.element_finder.finder.llm_element_finder.llm_element_finder.LLMElementFinder.find_link, curllm_core.element_finder.finder.llm_element_finder.llm_element_finder.LLMElementFinder._build_find_element_prompt, curllm_core.element_finder.finder.llm_element_finder.llm_element_finder.LLMElementFinder._call_llm, curllm_core.element_finder.finder.llm_element_finder.llm_element_finder.LLMElementFinder._parse_element_response

### curllm_core.orchestrators.master.MasterOrchestrator
> Master orchestrator for routing and coordinating complex tasks.

Features:
- Intelligent task type d
- **Methods**: 19
- **Key Methods**: curllm_core.orchestrators.master.MasterOrchestrator.__init__, curllm_core.orchestrators.master.MasterOrchestrator.orchestrate, curllm_core.orchestrators.master.MasterOrchestrator.analyze_task, curllm_core.orchestrators.master.MasterOrchestrator._detect_by_keywords, curllm_core.orchestrators.master.MasterOrchestrator._detect_with_llm, curllm_core.orchestrators.master.MasterOrchestrator._detect_subtasks, curllm_core.orchestrators.master.MasterOrchestrator._detect_capabilities, curllm_core.orchestrators.master.MasterOrchestrator.plan_execution, curllm_core.orchestrators.master.MasterOrchestrator.execute_plan, curllm_core.orchestrators.master.MasterOrchestrator._execute_main_task

### curllm_logs.run_logger.RunLogger
> Markdown run logger for step-by-step diagnostics (with TOC and images).

Usage:
    logger = RunLogg
- **Methods**: 18
- **Key Methods**: curllm_logs.run_logger.RunLogger.__init__, curllm_logs.run_logger.RunLogger._write, curllm_logs.run_logger.RunLogger.log_heading, curllm_logs.run_logger.RunLogger.log_text, curllm_logs.run_logger.RunLogger.log_kv, curllm_logs.run_logger.RunLogger.log_code, curllm_logs.run_logger.RunLogger.log_image, curllm_logs.run_logger.RunLogger.log_table, curllm_logs.run_logger.RunLogger.log_form_summary, curllm_logs.run_logger.RunLogger.log_step_result

### curllm_core.extraction_orchestrator.extraction_orchestrator.ExtractionOrchestrator
> Multi-phase extraction orchestrator with full LLM transparency
- **Methods**: 18
- **Key Methods**: curllm_core.extraction_orchestrator.extraction_orchestrator.ExtractionOrchestrator.__init__, curllm_core.extraction_orchestrator.extraction_orchestrator.ExtractionOrchestrator.orchestrate, curllm_core.extraction_orchestrator.extraction_orchestrator.ExtractionOrchestrator._phase_detection, curllm_core.extraction_orchestrator.extraction_orchestrator.ExtractionOrchestrator._phase_strategy, curllm_core.extraction_orchestrator.extraction_orchestrator.ExtractionOrchestrator._phase_navigation, curllm_core.extraction_orchestrator.extraction_orchestrator.ExtractionOrchestrator._phase_form_filling, curllm_core.extraction_orchestrator.extraction_orchestrator.ExtractionOrchestrator._phase_extraction, curllm_core.extraction_orchestrator.extraction_orchestrator.ExtractionOrchestrator._phase_validation, curllm_core.extraction_orchestrator.extraction_orchestrator.ExtractionOrchestrator._build_detection_prompt, curllm_core.extraction_orchestrator.extraction_orchestrator.ExtractionOrchestrator._build_strategy_prompt

### curllm_core.orchestrators.auth.AuthOrchestrator
> Specialized orchestrator for authentication tasks.

Features:
- LLM-driven element finding (primary)
- **Methods**: 18
- **Key Methods**: curllm_core.orchestrators.auth.AuthOrchestrator.__init__, curllm_core.orchestrators.auth.AuthOrchestrator._find_auth_element, curllm_core.orchestrators.auth.AuthOrchestrator.orchestrate, curllm_core.orchestrators.auth.AuthOrchestrator._parse_credentials, curllm_core.orchestrators.auth.AuthOrchestrator._detect_auth_method, curllm_core.orchestrators.auth.AuthOrchestrator._detect_platform, curllm_core.orchestrators.auth.AuthOrchestrator._standard_login, curllm_core.orchestrators.auth.AuthOrchestrator._two_factor_login, curllm_core.orchestrators.auth.AuthOrchestrator._oauth_login, curllm_core.orchestrators.auth.AuthOrchestrator._handle_2fa

### curllm_core.validation.task_validator.task_validator.task_validator.TaskValidator
> Multi-strategy task completion validator.

Usage:
    validator = TaskValidator(llm)
    report = aw
- **Methods**: 18
- **Key Methods**: curllm_core.validation.task_validator.task_validator.task_validator.TaskValidator.__init__, curllm_core.validation.task_validator.task_validator.task_validator.TaskValidator.register_custom_validator, curllm_core.validation.task_validator.task_validator.task_validator.TaskValidator.validate, curllm_core.validation.task_validator.task_validator.task_validator.TaskValidator._validate_structural, curllm_core.validation.task_validator.task_validator.task_validator.TaskValidator._validate_rules, curllm_core.validation.task_validator.task_validator.task_validator.TaskValidator._validate_schema, curllm_core.validation.task_validator.task_validator.task_validator.TaskValidator._validate_dom_diff, curllm_core.validation.task_validator.task_validator.task_validator.TaskValidator._validate_visual, curllm_core.validation.task_validator.task_validator.task_validator.TaskValidator._validate_semantic, curllm_core.validation.task_validator.task_validator.task_validator.TaskValidator._calculate_overall_score

### curllm_core.streamware.components.bql.parser.BQLParser
> Parser for Browser Query Language.

Supports:
- GraphQL-like query syntax
- Mutation blocks for acti
- **Methods**: 17
- **Key Methods**: curllm_core.streamware.components.bql.parser.BQLParser.__init__, curllm_core.streamware.components.bql.parser.BQLParser.parse, curllm_core.streamware.components.bql.parser.BQLParser._preprocess, curllm_core.streamware.components.bql.parser.BQLParser._tokenize, curllm_core.streamware.components.bql.parser.BQLParser._match, curllm_core.streamware.components.bql.parser.BQLParser._consume, curllm_core.streamware.components.bql.parser.BQLParser._parse_query_block, curllm_core.streamware.components.bql.parser.BQLParser._parse_mutation_block, curllm_core.streamware.components.bql.parser.BQLParser._parse_operation, curllm_core.streamware.components.bql.parser.BQLParser._parse_action

### curllm_core.orchestrators.social.SocialMediaOrchestrator
> Specialized orchestrator for social media automation.

Features:
- LLM-driven element finding (prima
- **Methods**: 17
- **Key Methods**: curllm_core.orchestrators.social.SocialMediaOrchestrator._find_element_with_llm, curllm_core.orchestrators.social.SocialMediaOrchestrator.__init__, curllm_core.orchestrators.social.SocialMediaOrchestrator.orchestrate, curllm_core.orchestrators.social.SocialMediaOrchestrator._detect_platform, curllm_core.orchestrators.social.SocialMediaOrchestrator._parse_social_intent, curllm_core.orchestrators.social.SocialMediaOrchestrator._perform_login, curllm_core.orchestrators.social.SocialMediaOrchestrator._create_post, curllm_core.orchestrators.social.SocialMediaOrchestrator._send_message, curllm_core.orchestrators.social.SocialMediaOrchestrator._like_content, curllm_core.orchestrators.social.SocialMediaOrchestrator._follow_user

### curllm_core.bql.bql_parser.BQLParser
- **Methods**: 17
- **Key Methods**: curllm_core.bql.bql_parser.BQLParser.__init__, curllm_core.bql.bql_parser.BQLParser.parse, curllm_core.bql.bql_parser.BQLParser._preprocess, curllm_core.bql.bql_parser.BQLParser._tokenize, curllm_core.bql.bql_parser.BQLParser._match, curllm_core.bql.bql_parser.BQLParser._consume, curllm_core.bql.bql_parser.BQLParser._parse_query_block, curllm_core.bql.bql_parser.BQLParser._parse_mutation_block, curllm_core.bql.bql_parser.BQLParser._parse_operation, curllm_core.bql.bql_parser.BQLParser._parse_action

### bql.parser.bql_parser.BQLParser
> Parser for Browser Query Language
- **Methods**: 17
- **Key Methods**: bql.parser.bql_parser.BQLParser.__init__, bql.parser.bql_parser.BQLParser.parse, bql.parser.bql_parser.BQLParser._preprocess, bql.parser.bql_parser.BQLParser._tokenize, bql.parser.bql_parser.BQLParser._match, bql.parser.bql_parser.BQLParser._consume, bql.parser.bql_parser.BQLParser._parse_query_block, bql.parser.bql_parser.BQLParser._parse_mutation_block, bql.parser.bql_parser.BQLParser._parse_operation, bql.parser.bql_parser.BQLParser._parse_action

### scripts.dev_watcher.DevWatcher
> Development file watcher with auto-reload capabilities
- **Methods**: 16
- **Key Methods**: scripts.dev_watcher.DevWatcher.__init__, scripts.dev_watcher.DevWatcher.log, scripts.dev_watcher.DevWatcher.classify_change, scripts.dev_watcher.DevWatcher.should_debounce, scripts.dev_watcher.DevWatcher.run_command, scripts.dev_watcher.DevWatcher.handle_dependency_change, scripts.dev_watcher.DevWatcher.handle_source_change, scripts.dev_watcher.DevWatcher.handle_test_change, scripts.dev_watcher.DevWatcher.handle_config_change, scripts.dev_watcher.DevWatcher.clear_pycache

### functions.safety.validate.InputValidator
> Chainable input validator.

Example:
    validator = InputValidator()
    result = validator.validat
- **Methods**: 16
- **Key Methods**: functions.safety.validate.InputValidator.__init__, functions.safety.validate.InputValidator.validate, functions.safety.validate.InputValidator.not_none, functions.safety.validate.InputValidator.is_string, functions.safety.validate.InputValidator.not_empty, functions.safety.validate.InputValidator.min_length, functions.safety.validate.InputValidator.max_length, functions.safety.validate.InputValidator.matches, functions.safety.validate.InputValidator.not_matches, functions.safety.validate.InputValidator.is_numeric

## Data Transformation Functions

Key functions that process and transform data:

### examples_streamware.example_5_multi_format_export
> Example 5: Extract data and export in multiple formats

New: Multicast pattern for multiple outputs
- **Output to**: monitoring.website_monitor.print, None.run, monitoring.website_monitor.print, curllm_core.streamware.flow.flow, curllm_core.streamware.patterns.multicast.multicast

### examples_streamware.example_6_batch_processing
> Example 6: Process multiple URLs with split/join

New: Advanced pattern for batch operations
- **Output to**: monitoring.website_monitor.print, None.run, monitoring.website_monitor.print, curllm_core.streamware.patterns.join.join, None.with_data

### examples_streamware.example_14_transform_pipeline
> Example 14: Data transformation pipeline

New: Multiple transformations in sequence
- **Output to**: monitoring.website_monitor.print, None.run, monitoring.website_monitor.print, None.with_data, curllm_core.streamware.flow.flow

### examples.detection.atomic_query_example.example_multi_format_export
> Example 4: Export to multiple formats
- **Output to**: monitoring.website_monitor.print, monitoring.website_monitor.print, DataExporter, Path, output_dir.mkdir

### captcha.playwright_bql_framework._parse_actions_from_llm
> Robustly parse a JSON array of action dicts from an LLM output string or list.
- Accepts list direct
- **Output to**: isinstance, curllm_server.executor.curllm_executor.CurllmExecutor._strip_fences, enumerate, isinstance, s.strip

### examples.url_resolver.example_complete_flow.parse_command
> Parsuje polecenie użytkownika i wyciąga:
- domenę
- cel (kontakt, formularz, etc.)
- dane do wypełni
- **Output to**: command.lower, re.search, re.search, any, re.search

### curllm_core.llm_guided_extractor.LLMGuidedExtractor._parse_prices_with_llm
> Parse prices using LLM - NO REGEX
- **Output to**: isinstance, p.get, json.dumps, self.llm.ainvoke, response.find

### curllm_core.runtime.parse_runtime_from_instruction
> Extract runtime params from JSON-like instruction.
Accepts schemas like {instruction:"...", params:{
- **Output to**: dict, instruction.strip, os.getenv, s.startswith, json.loads

### curllm_core.validation_utils.should_validate
- **Output to**: None.lower, any, any, isinstance, data.get

### curllm_logs.log_writer.MarkdownLogWriter._write_parsed_section
> Write parsed command info
- **Output to**: f.write, f.write, f.write, f.write, f.write

### curllm_core.config_logger.format_config_for_cli
> Format configuration for CLI output (e.g., --config flag).

Returns:
    List of formatted strings f
- **Output to**: curllm_core.config_logger.get_all_config_variables, lines.append, lines.append, lines.append, lines.append

### curllm_core.config_logger.validate_config
> Validate configuration and return list of warnings/errors.

Returns:
    List of warning/error messa
- **Output to**: curllm_core.config_logger.get_all_config_variables, warnings.append, warnings.append, warnings.append, warnings.append

### curllm_core.llm_filter_validator.LLMFilterValidator.validate_product
> Validate single product against semantic criteria

Args:
    product: {name, price, url, description
- **Output to**: self._format_product_text, json.loads, self._log, json.dumps, self.llm.ainvoke

### curllm_core.llm_filter_validator.LLMFilterValidator.validate_batch
> Validate multiple products (batch processing)

Returns list of validation results for each product.
- **Output to**: range, len, results.extend, self._validate_batch_internal

### curllm_core.llm_filter_validator.LLMFilterValidator._validate_batch_internal
> Validate a small batch of products in single LLM call
- **Output to**: None.join, json.loads, None.join, self.llm.ainvoke, isinstance

### curllm_core.llm_filter_validator.LLMFilterValidator._format_product_text
> Format product data for LLM analysis
- **Output to**: None.join, parts.append, product.get, parts.append, parts.append

### curllm_core.instruction_parser.InstructionParser.parse
> Parse instruction into structured criteria

Returns:
    {
        "criteria": {
            "price"
- **Output to**: instruction.lower, self._parse_numeric_criteria, self._parse_numeric_criteria, self._parse_numeric_criteria, self._parse_semantic

### curllm_core.instruction_parser.InstructionParser._parse_numeric_criteria
> Parse numeric criteria (price, weight, volume)
- **Output to**: re.search, len, float, float, match.group

### curllm_core.instruction_parser.InstructionParser._parse_semantic
> Parse semantic keywords
- **Output to**: self.semantic_keywords.items, found.append

### curllm_core.instruction_parser.InstructionParser.format_criteria_summary
> Generate human-readable summary of criteria
- **Output to**: None.join, parts.append, parts.append, parts.append, parts.append

### curllm_core.error_handler.format_user_friendly_error
> Convert technical error to user-friendly message.

Args:
    error: The exception that occurred
    
- **Output to**: functions.js.safety.str, ERROR_MAPPINGS.items, pattern.lower, error_str.lower, friendly_error.copy

### curllm_core.error_handler.format_error_for_logging
> Format error for structured logging.

Args:
    error: The exception
    context: Additional context
- **Output to**: curllm_core.error_handler.format_user_friendly_error, None.join, lines.insert

### curllm_core.iterative_extractor.IterativeExtractor._validate_results
> Validate extracted results against instruction criteria.

Checks:
1. Products have required fields (
- **Output to**: set, enumerate, None.strip, product.get, any

### curllm_core.atomic_functions.AtomicFunctionExecutor._transform_value
> Transform extracted value according to type and transform spec
- **Output to**: self._extract_price, float, value.startswith, self._extract_url, re.sub

### curllm_core.atomic_functions.AtomicFunctionExecutor.validate_entities
> Validate extracted entities against field specifications.

Returns only entities that pass validatio
- **Output to**: self._log, validated.append, entity.get, len, len

## Behavioral Patterns

### recursion_list
- **Type**: recursion
- **Confidence**: 0.90
- **Functions**: functions.registry.FunctionRegistry.list

### recursion_list
- **Type**: recursion
- **Confidence**: 0.90
- **Functions**: functions.patterns.registry.PatternRegistry.list

### state_machine_ProxyStateManager
- **Type**: state_machine
- **Confidence**: 0.70
- **Functions**: curllm_core.proxy.ProxyStateManager.__init__, curllm_core.proxy.ProxyStateManager.next_index

### state_machine_RetryContext
- **Type**: state_machine
- **Confidence**: 0.70
- **Functions**: curllm_core.retry.RetryContext.__init__, curllm_core.retry.RetryContext.__aenter__, curllm_core.retry.RetryContext.__aexit__, curllm_core.retry.RetryContext.should_retry, curllm_core.retry.RetryContext.success

### state_machine_ProxyStateManager
- **Type**: state_machine
- **Confidence**: 0.70
- **Functions**: curllm_core.streamware.components.browser.proxy.ProxyStateManager.__init__, curllm_core.streamware.components.browser.proxy.ProxyStateManager._load_state, curllm_core.streamware.components.browser.proxy.ProxyStateManager._save_state, curllm_core.streamware.components.browser.proxy.ProxyStateManager.next_index

### state_machine_SafeExtractor
- **Type**: state_machine
- **Confidence**: 0.70
- **Functions**: functions.safety.wrapper.SafeExtractor.__init__, functions.safety.wrapper.SafeExtractor.__enter__, functions.safety.wrapper.SafeExtractor.__exit__, functions.safety.wrapper.SafeExtractor.call, functions.safety.wrapper.SafeExtractor.has_errors

## Public API Surface

Functions exposed as public API (no underscore prefix):

- `curllm_core.streamware.components.form.orchestrator.orchestrate_form_fill` - 236 calls
- `curllm_core.execution.executor.curllm_executor.CurllmExecutor.execute_workflow` - 233 calls
- `curllm_core.form_fill.deterministic_form_fill` - 222 calls
- `curllm_core.running.runner.run_task` - 161 calls
- `curllm_core.result_evaluator.evaluate_run_success` - 106 calls
- `curllm_core.llm_planner.generate_action` - 103 calls
- `curllm_core.multi_criteria_filter.MultiCriteriaFilter.filter_products` - 77 calls
- `extension.extension.CurllmExtension.curllmExtension` - 72 calls
- `curllm_core.navigation.open_page_with_prechecks` - 72 calls
- `curllm_core.hierarchical.planner.hierarchical_plan` - 69 calls
- `scripts.analyze_deps.main` - 64 calls
- `curllm_core.deprecated.cli_orchestrator.main` - 59 calls
- `scripts.analyze_dependencies.main` - 57 calls
- `curllm_core.proxy.resolve_proxy` - 56 calls
- `wordpress_batch.batch_create_posts` - 54 calls
- `examples.streamware.streamware_quickstart.main` - 53 calls
- `examples.currency.currency_example.main` - 52 calls
- `curllm_core.browser_setup.setup_playwright` - 51 calls
- `curllm_core.dom_toolkit.orchestrator.task_router.ExtractionOrchestrator.extract` - 47 calls
- `examples.detection.llm_heuristics_example.main` - 46 calls
- `curllm_core.server.proxy_health` - 46 calls
- `curllm_core.remediation.remediate_if_empty` - 46 calls
- `curllm_core.cli.feedback.main` - 46 calls
- `curllm_core.vision_form_analysis.create_vision_decision_tree` - 45 calls
- `curllm_core.deprecated.llm_form_orchestrator.execute_form_plan` - 45 calls
- `curllm_core.orchestration.orchestrator.orchestrator.Orchestrator.execute` - 45 calls
- `curllm_core.iterative_extractor.IterativeExtractor.run` - 44 calls
- `curllm_core.url_resolution.resolver.UrlResolver.resolve` - 44 calls
- `pricing.app.api_compare_stream` - 43 calls
- `curllm_core.vision_form_analysis.analyze_form_fields_vision` - 42 calls
- `scripts.find_hardcoded.generate_report` - 41 calls
- `captcha.allegro_captcha_solver.main` - 40 calls
- `curllm_core.progressive_context.build_progressive_context` - 40 calls
- `examples.url_resolver.example_complete_flow.execute_command` - 39 calls
- `curllm_core.planner_progress.progress_tick` - 39 calls
- `forms.app.api_bulk_stream` - 39 calls
- `examples.orchestration.semantic_query_example.example_semantic_vs_monolithic` - 37 calls
- `examples.llm-providers.multi_provider_benchmark.run_benchmark` - 37 calls
- `examples.benchmark_providers` - 36 calls
- `scripts.fix_missing_loggers.fix_missing_logger` - 36 calls

## System Interactions

How components interact:

```mermaid
graph TD
    execute_workflow --> parse_runtime_from_i
    execute_workflow --> join
    execute_workflow --> RunLogger
    execute_workflow --> log_heading
    execute_workflow --> log_all_config
    deterministic_form_f --> parse_form_pairs
    deterministic_form_f --> items
    deterministic_form_f --> get
    deterministic_form_f --> isinstance
    run_task --> lower
    run_task --> any
    run_task --> int
    run_task --> ToolRetryManager
    run_task --> range
    filter_products --> parse
    filter_products --> _log
    filter_products --> FilterStage
    filter_products --> len
    curllmExtension --> constructor
    curllmExtension --> init
    curllmExtension --> addListener
    curllmExtension --> handleMessage
    curllmExtension --> injectHelpers
    open_page_with_prech --> get
    open_page_with_prech --> bool
    open_page_with_prech --> log_kv
    open_page_with_prech --> new_page
    main --> print
    main --> find_python_files
    main --> parse_args
```

## Reverse Engineering Guidelines

1. **Entry Points**: Start analysis from the entry points listed above
2. **Core Logic**: Focus on classes with many methods
3. **Data Flow**: Follow data transformation functions
4. **Process Flows**: Use the flow diagrams for execution paths
5. **API Surface**: Public API functions reveal the interface

## Context for LLM

Maintain the identified architectural patterns and public API surface when suggesting changes.