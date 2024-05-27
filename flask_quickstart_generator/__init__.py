from .cli import main
from .css import DEMO_CSS
from .model import USER_MODEL
from .settings import APP_SETTINGS
from .cmd_handler import CmdHandler
from .html import BASE_HTML, FLASH_MESSAGE, DEMO_HTML_TEMPLATES
from .routes_ import (
    GITIGNORE,
    SEARCH_FORM,
    APP_STARTUP,
    ACCOUNT_UTILS,
    CACHING_CONSTANT,
    UPLOAD_FILES_FORM,
    VIEW_TEMPLATE_CODE,
    ADMIN_TEMPLATE_CODE,
    SEARCH_TEMPLATE_CODE,
    ACCOUNT_SETTINGS_FORM,
    ACCOUNT_SETTINGS_FORM,
    FILES_UPLOAD_TEMPLATE_CODE,
    ERROR_HANDLER_TEMPLATE_CODE,
    AUTHENTICATION_TEMPLATE_CODE,
    ACCOUNT_SETTINGS_TEMPLATE_CODE,
)


"""
op.create_table: Creates a new table.
op.drop_table: Drops an existing table.
op.add_column: Adds a new column to an existing table.
op.drop_column: Removes a column from an existing table.
op.alter_column: Modifies the definition of an existing column.
op.rename_table: Renames an existing table.
op.create_index: Creates an index on a table.
op.drop_index: Drops an index from a table.
op.create_foreign_key: Creates a foreign key constraint.
op.drop_foreign_key: Drops a foreign key constraint.
op.batch_alter_table: Used to make multiple alterations to a table within a single context, which is useful for databases that don't support transactional DDL.
"""