"""rename_content_to_body_in_posts

Revision ID: de156007f4e7
Revises: b631e65468ca
Create Date: 2026-05-13 17:27:01.707853

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de156007f4e7'
down_revision: Union[str, Sequence[str], None] = 'b631e65468ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
