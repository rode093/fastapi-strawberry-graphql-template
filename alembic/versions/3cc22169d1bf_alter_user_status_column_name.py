"""alter user status column name

Revision ID: 3cc22169d1bf
Revises: 809edc1f7cfd
Create Date: 2023-07-09 15:47:56.920981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cc22169d1bf'
down_revision = '809edc1f7cfd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('users', column_name='status',
                    new_column_name="status_code", default="NEW", nullable=False),
    op.create_foreign_key('fk_user_status', 'users',
                          'user_statuses', ['status_code'], ['code'])


def downgrade() -> None:
    op.alter_column('users', column_name='status_code',
                    new_column_name="status", default="NEW", nullable=False),
    op.drop_index('fk_user_status')
