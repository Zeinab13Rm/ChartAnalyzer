#!/bin/bash

# Project root
PROJECT_DIR="chart_analyzer"
mkdir -p "$PROJECT_DIR"/{src,tests/{unit,integration,e2e}}

# Domain layer
mkdir -p "$PROJECT_DIR"/src/domain/{entities,value_objects,ports,services,exceptions}

# Application layer
mkdir -p "$PROJECT_DIR"/src/application/{use_cases,services}

# Infrastructure layer
mkdir -p "$PROJECT_DIR"/src/infrastructure/{adapters,api/fastapi,services}

# Create empty Python files with __init__.py
touch "$PROJECT_DIR"/src/{domain,application,infrastructure}/__init__.py
touch "$PROJECT_DIR"/src/domain/{entities,value_objects,ports,services,exceptions}/__init__.py
touch "$PROJECT_DIR"/src/application/{use_cases,services}/__init__.py
touch "$PROJECT_DIR"/src/infrastructure/{adapters,api,services}/__init__.py
touch "$PROJECT_DIR"/src/infrastructure/api/fastapi/__init__.py

# Main domain files
touch "$PROJECT_DIR"/src/domain/entities/{chart_image,chart_analysis}.py
touch "$PROJECT_DIR"/src/domain/value_objects/trend_summary.py
touch "$PROJECT_DIR"/src/domain/ports/{image_storage,model_integration}.py
touch "$PROJECT_DIR"/src/domain/services/chart_validation.py
touch "$PROJECT_DIR"/src/domain/exceptions/domain_errors.py

# Main application files
touch "$PROJECT_DIR"/src/application/use_cases/{upload_image,general_analysis,specific_question,continue_convo}.py
touch "$PROJECT_DIR"/src/application/services/conversation_ctx.py

# Main infrastructure files
touch "$PROJECT_DIR"/src/infrastructure/adapters/{mongodb_image_storage,model_adapter}.py
touch "$PROJECT_DIR"/src/infrastructure/api/fastapi/{routes,schemas}.py
touch "$PROJECT_DIR"/src/infrastructure/services/image_preprocessor.py

# Entry point and test files
touch "$PROJECT_DIR"/main.py
touch "$PROJECT_DIR"/tests/{unit,integration,e2e}/__init__.py

echo "Project structure created at: $PROJECT_DIR"
